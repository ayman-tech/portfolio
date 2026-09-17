# Ayman Sayed — Portfolio

A fast, static portfolio built with **Astro, TypeScript, and CSS**, ready for GitHub Pages at **https://aymanai.com**. Includes projects, experience, education, skills, personal updates, and a persistent dark/light theme. No Python server or external services are required.

## Develop locally

Use Node.js 24 (`nvm use` if you use nvm).

```sh
npm ci
npm run dev
```

Open http://localhost:4321. To check the production output:

```sh
npm run check
npm test
npm run build
npm run preview
```

The deployable website is generated in `dist/`. The repository's source files are not the deployment artifact.

## Edit your content

- **Personal updates:** `src/data/updates.ts`
- **Profile, projects, experience, education, skills:** `src/data/portfolio.ts`
- **Portrait:** `src/assets/profile.png` (Astro creates optimized WebP versions automatically)
- **Colors, spacing, and responsive layout:** `src/styles/global.css`

### Add an update

Add an object to the top of the `UPDATES` array. Updates appear in the order you write them. The date is the **event or publication date**, so future dates are welcome and render immediately. No scheduling service is needed.

Example entries below are templates only; replace all example text, dates, and URLs with real details before publishing:

```ts
export const UPDATES: Update[] = [
  {
    date: '2027-01-15',
    title: 'Attending [conference name]',
    description: 'I’ll be attending [conference] in [location].',
    link: 'https://example.com/conference',
  },
  {
    date: '2027-02-10',
    title: '[Paper title] will be published in [venue]',
    link: 'https://example.com/paper',
  },
  {
    title: 'Reinforcement learning for multi-year ENSO events',
    description: 'Working on a reinforcement learning project to drive climate modes toward more multi-year El Niño or La Niña events.',
  },
];
```

Only `title` is required. Omit `date` for ongoing work, which displays **Ongoing**. `description` and `link` are optional. Use real calendar dates in `YYYY-MM-DD` format and complete `https://` or `http://` links; invalid entries produce a clear build error. Dates display consistently across time zones.

Use an empty array (`export const UPDATES: Update[] = [];`) to display a quiet empty state. Entries remain visible until edited or removed. There is no admin login: edit the file locally or in GitHub, commit, and push to `master` to publish through the workflow.

The existing `ayman_resume.txt` is retained as a source document and is not published as a download.

## Deploy on GitHub Pages

The workflow in `.github/workflows/deploy.yml` checks, tests, builds, and uploads the site. Pull requests are checked without deploying. Pushes to **master** and manual runs on master deploy to the `github-pages` environment.

1. Push this repository to `ayman-tech/portfolio`, including `package-lock.json`.
2. In **Settings → Pages → Build and deployment**, select **GitHub Actions**.
3. Set the **Custom domain** to `aymanai.com` and save it. The Astro configuration uses this domain with no `/portfolio` prefix. A `CNAME` file is not required for this Actions-based deployment; the Pages setting controls the domain.
4. Verify ownership of `aymanai.com` in your GitHub account's Pages settings using the TXT record GitHub provides.
5. At your DNS provider, point the apex (`@`) at GitHub Pages using an ALIAS/ANAME to `ayman-tech.github.io` if supported, or GitHub's documented A records:

   | Type | Host | Value |
   | --- | --- | --- |
   | A | @ | 185.199.108.153 |
   | A | @ | 185.199.109.153 |
   | A | @ | 185.199.110.153 |
   | A | @ | 185.199.111.153 |
   | CNAME | www | ayman-tech.github.io |

   Replace conflicting apex/`www` records from the old host, including any old AAAA records. Preserve records for your other services, including `triage.aymanai.com`, `deeprag.aymanai.com`, and email. If using IPv6, use GitHub's current documented AAAA records.
6. Run **Actions → Deploy portfolio to GitHub Pages → Run workflow**, or push to master. Once GitHub's DNS check and certificate provisioning succeed, enable **Enforce HTTPS**.
7. Verify https://aymanai.com on desktop and mobile, including the theme toggle, navigation, portrait, updates, and project links. Keep the old host available until the domain migration is verified.

DNS and GitHub repository settings are not changed by editing these files. To roll back a website change, revert the relevant commit and push again. To roll back hosting, restore the previous DNS records while the old server is still available.

References: [Astro GitHub Pages deployment](https://docs.astro.build/en/guides/deploy/github/), [GitHub custom domain configuration](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [domain verification](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages).
