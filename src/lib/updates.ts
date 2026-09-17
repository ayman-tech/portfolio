export interface Update {
  title: string;
  date?: string;
  description?: string;
  link?: string;
}

export function formatUpdateDate(date?: string): string {
  if (date === undefined) return 'Ongoing';
  const parsed = new Date(`${date}T00:00:00Z`);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date) || !Number.isFinite(parsed.getTime()) ||
      parsed.toISOString().slice(0, 10) !== date) {
    throw new Error(`Invalid update date "${date}". Use a real calendar date in YYYY-MM-DD format.`);
  }
  return new Intl.DateTimeFormat('en-US', {
    month: 'short', day: 'numeric', year: 'numeric', timeZone: 'UTC',
  }).format(parsed);
}

export function validateUpdates(updates: Update[]): Update[] {
  for (const update of updates) {
    if (!update.title.trim()) throw new Error('Each update needs a title.');
    formatUpdateDate(update.date);
    if (update.link !== undefined) {
      let url: URL;
      try { url = new URL(update.link); }
      catch { throw new Error(`Invalid update link for "${update.title}". Use an https:// or http:// URL.`); }
      if (!['https:', 'http:'].includes(url.protocol)) {
        throw new Error(`Invalid update link protocol for "${update.title}". Use https:// or http://.`);
      }
    }
  }
  return updates;
}
