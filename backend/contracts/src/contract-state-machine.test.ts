import { test } from 'node:test';
import assert from 'node:assert/strict';
import { CONTRACT_EVENTS, CONTRACT_STATES, InvalidTransitionError, canTransition, isTerminal, transition } from './contract-state-machine.ts';

test('happy path', () => {
  let s = transition('draft', 'send');
  s = transition(s, 'recipient_signed');
  assert.equal(s, 'in_progress');
  assert.equal(transition(s, 'all_signed'), 'completed');
});

test('terminal states accept nothing', () => {
  for (const s of CONTRACT_STATES.filter(isTerminal)) {
    for (const e of CONTRACT_EVENTS) assert.equal(canTransition(s, e), false, `${s}/${e}`);
  }
  assert.deepEqual(CONTRACT_STATES.filter(isTerminal).sort(), ['completed', 'declined', 'expired', 'voided']);
});

test('invalid transition throws typed error', () => {
  assert.throws(() => transition('draft', 'all_signed'), InvalidTransitionError);
  assert.throws(() => transition('completed', 'void'), /not allowed/);
});
