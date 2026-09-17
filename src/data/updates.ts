import type { Update } from '../lib/updates';

// Displayed in this order. Add your latest announcement at the top.
// date is the conference/publication/event date (YYYY-MM-DD), not the posting date.
// Omit date for ongoing work. description and link are optional.
// See README.md for conference and publication examples.
export const UPDATES: Update[] = [
  {
    title: 'Reinforcement learning for multi-year ENSO events',
    description:
      'Working on a reinforcement learning project to drive climate modes toward more multi-year El Niño or La Niña events.',
  },
];
