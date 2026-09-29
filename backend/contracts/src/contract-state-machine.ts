export const CONTRACT_STATES = [
  'draft', 'sent', 'in_progress', 'completed', 'declined', 'voided', 'expired',
] as const;
export type ContractState = (typeof CONTRACT_STATES)[number];

export const CONTRACT_EVENTS = [
  'send', 'recipient_signed', 'all_signed', 'decline', 'void', 'expire', 'correct',
] as const;
export type ContractEvent = (typeof CONTRACT_EVENTS)[number];

/** completed/declined/voided/expired are terminal: a signed contract is immutable; "correcting" one creates a new draft version. */
const TRANSITIONS: Record<ContractState, Partial<Record<ContractEvent, ContractState>>> = {
  draft: { send: 'sent', void: 'voided' },
  sent: { recipient_signed: 'in_progress', all_signed: 'completed', decline: 'declined', void: 'voided', expire: 'expired', correct: 'draft' },
  in_progress: { recipient_signed: 'in_progress', all_signed: 'completed', decline: 'declined', void: 'voided', expire: 'expired' },
  completed: {},
  declined: {},
  voided: {},
  expired: {},
};

export class InvalidTransitionError extends Error {
  readonly from: ContractState;
  readonly event: ContractEvent;
  constructor(from: ContractState, event: ContractEvent) {
    super(`event "${event}" not allowed in state "${from}"`);
    this.from = from;
    this.event = event;
  }
}

export function canTransition(from: ContractState, event: ContractEvent): boolean {
  return TRANSITIONS[from][event] !== undefined;
}

export function transition(from: ContractState, event: ContractEvent): ContractState {
  const to = TRANSITIONS[from][event];
  if (!to) throw new InvalidTransitionError(from, event);
  return to;
}

export const isTerminal = (s: ContractState): boolean => Object.keys(TRANSITIONS[s]).length === 0;

/**
 * Persist with a compare-and-set so two concurrent transitions cannot both win:
 *   UPDATE contracts SET state = $to, version = version + 1
 *   WHERE id = $id AND state = $from AND version = $v
 * 0 rows updated => someone else moved it; re-read and retry or fail.
 */
