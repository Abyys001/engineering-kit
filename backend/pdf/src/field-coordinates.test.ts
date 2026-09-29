import { test } from 'node:test';
import assert from 'node:assert/strict';
import { normalizeRotation, toPdfRect, toRelativeRect, type PageGeometry, type RelativeRect } from './field-coordinates.ts';

const near = (a: number, b: number) => assert.ok(Math.abs(a - b) < 1e-9, `${a} vs ${b}`);
const rect: RelativeRect = { page: 0, x: 0.1, y: 0.2, width: 0.3, height: 0.05 };

test('rotate 0, offset CropBox: top-left fraction → bottom-left points', () => {
  const g: PageGeometry = { box: [10, 20, 610, 820], rotate: 0 }; // 600×800 at offset
  const p = toPdfRect(rect, g);
  near(p.x, 10 + 60); near(p.width, 180); near(p.height, 40);
  near(p.y, 20 + (1 - 0.2 - 0.05) * 800);
});

test('round trip for every rotation and an offset box', () => {
  for (const rotate of [0, 90, 180, 270] as const) {
    const g: PageGeometry = { box: [5, 7, 605, 907], rotate };
    const back = toRelativeRect(toPdfRect(rect, g), 0, g);
    for (const k of ['x', 'y', 'width', 'height'] as const) near(back[k], rect[k]);
  }
});

test('rotate 90: displayed top-left corner is the unrotated bottom-left', () => {
  const g: PageGeometry = { box: [0, 0, 600, 800], rotate: 90 };
  const p = toPdfRect({ page: 0, x: 0, y: 0, width: 0.1, height: 0.1 }, g);
  near(p.x, 0); near(p.y, 0);
  near(p.width, 0.1 * 600); near(p.height, 0.1 * 800);
});

test('rejects out-of-bounds and non-finite rects', () => {
  const g: PageGeometry = { box: [0, 0, 600, 800], rotate: 0 };
  assert.throws(() => toPdfRect({ ...rect, x: 0.9 }, g), RangeError);
  assert.throws(() => toPdfRect({ ...rect, width: NaN }, g), RangeError);
  assert.throws(() => toPdfRect({ ...rect, width: 0 }, g), RangeError);
});

test('rotation normalisation', () => {
  assert.equal(normalizeRotation(-90), 270);
  assert.equal(normalizeRotation(450), 90);
});
