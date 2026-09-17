import { test } from 'node:test';
import assert from 'node:assert/strict';
import { formatUpdateDate, validateUpdates } from '../src/lib/updates.ts';

test('an undated research update is ongoing, without inventing a date', () => {
  assert.equal(formatUpdateDate(), 'Ongoing');
  assert.doesNotThrow(() => validateUpdates([{ title: 'Research in progress' }]));
});

test('conference and publication dates retain their calendar day across time zones', () => {
  for (const timezone of ['America/Los_Angeles', 'Pacific/Kiritimati']) {
    const previous = process.env.TZ;
    try {
      process.env.TZ = timezone;
      assert.equal(formatUpdateDate('2026-12-01'), 'Dec 1, 2026');
      assert.equal(formatUpdateDate('2028-02-29'), 'Feb 29, 2028');
    } finally {
      if (previous === undefined) delete process.env.TZ;
      else process.env.TZ = previous;
    }
  }
});

test('invalid and ambiguous dates fail with an actionable build error', () => {
  for (const date of ['2026-02-29', '2026-04-31', '12/01/2026', '', '2026-13-01']) {
    assert.throws(() => formatUpdateDate(date), /YYYY-MM-DD/);
  }
});

test('empty lists and optional links are supported; unsafe links are rejected', () => {
  assert.deepEqual(validateUpdates([]), []);
  assert.doesNotThrow(() => validateUpdates([{ title: 'Conference', date: '2026-12-01', link: 'https://example.com/conference' }]));
  assert.throws(() => validateUpdates([{ title: 'Paper', link: 'javascript:alert(1)' }]), /protocol/);
  assert.throws(() => validateUpdates([{ title: 'Paper', link: 'not a URL' }]), /Invalid update link/);
  assert.throws(() => validateUpdates([{ title: '   ' }]), /title/);
});
