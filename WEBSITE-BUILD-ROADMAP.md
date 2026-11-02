# Prosperity Life School: Website Build Roadmap (v2)

Based on the three client documents:
- **A. Developer Instructions** (the brief: main site as authority hub, 9 nav items, SEO, CRM)
- **B. Website Content 1** (the "Main Website Content": final copy for the hub site)
- **C. Website Content** (the 7-page, internetlifestylehub-style community site: Home, Memberships, Masterclass, Join, Stories, TV, Reads)

## 1. What I understood

The brief (A) wants **one main website** that builds trust, explains the whole ecosystem, and routes visitors to the right funnel, without replacing the focused campaign landing pages. Copy B fits that brief exactly. Copy C is a **different site concept** (a community and membership site with a masterclass funnel, video sales page, story feed, video library and books). It is not the same thing as A and B.

I would build **A + B as the main website**, and treat **C as a second layer** (a "Community" section, or a separate site later) rather than mixing the two on day one.

## 2. Conflicts to settle before design starts

| # | Topic | A + B (hub site) | C (community site) | My recommendation |
|---|---|---|---|---|
| 1 | Site concept | Authority and lead hub, 9 nav items | 7 pages, nav: Stories · TV · Reads · Memberships · Login | Hub first. Add C's pages as a "Community" area in Phase 3 |
| 2 | Membership tiers | Silver (Blueprint), Gold (Navigator), Diamond (Mastery) | Silver, Gold, Diamond **certification**, Platinum (invite-only) | Pick 3 or 4 tiers and one set of names |
| 3 | Colours | Navy, green, gold, white | Navy `#011D43`, gold `#D09C32`, white (no green) | Navy + gold + white as the base with green as a small accent, to match the logo and the existing landing pages |
| 4 | Fonts | Poppins or Arial | not stated | Poppins (body) with the serif heading we already use for landing pages, or Poppins only. Please confirm |
| 5 | ™ symbol | "Do not use ™ unless authorised" | n/a | The landing pages I built use "Retirement Clarity Call™". Confirm whether that is authorised, else I remove it |
| 6 | Primary CTA | "Take Free Assessment" | "Join the Community" / "Free Masterclass" | One primary CTA for the whole site: the Free Assessment. Masterclass is secondary |
| 7 | Prices | Not specified | Silver Rs 7,999 / 9,999 / 13,999 incl. GST on Join page | Confirm Silver prices are public; keep Gold/Diamond price-after-call |

## 3. Risky copy in document C that I recommend changing

These conflict with the client's own earlier rules (no fake scarcity, no income or outcome promises) and with Meta/financial-promotion norms.
- **Countdown + "seats left" + "[X] seats taken today"**: only use if real and live. Otherwise remove.
- **Join page offer hidden for a 5-minute timer, "before it's taken down"**: this is artificial pressure. Recommend showing the offer plainly.
- **"₹1,999 FREE · Limited time"**: confirm it is a real value claim.
- **"₹52 lakh in 9 months", "earn your first extra ₹1 lakh a month"**: income and result claims. Need verification, permission and an "individual results vary" note, or removal.
- **Brackets `[10,000+]`, `[X]+` reviews, Trustpilot, Hall of Fame**: placeholders must not go live. Existing doc numbers elsewhere say 12,000+ educated and 500+ client families, while C says 10,000+ families guided. **Use one verified set of numbers everywhere.**
- Standard guardrails still apply: no guaranteed returns, show only verified credentials, do not say "SEBI registered" without registration details.

## 4. Site map (hub site, from A + B)

**Header:** Home · About · Programs · Financial Planning · Financial Services · Financial Literacy · Income Opportunities · Resources · Contact, plus the button **Take Free Assessment**.

| Section | Pages | Sends traffic to |
|---|---|---|
| Home | 1 | the 8 pathway cards below |
| About | Dr Maria, About PLS | trust → assessment |
| Programs | overview, Silver (Blueprint), Gold (Navigator), Diamond (Mastery), Foundation Masterclass, Workshops | membership / masterclass pages |
| Financial Planning | Financial Clarity, Comprehensive Planning, Retirement | **existing landing pages** (clarity call, retirement) |
| Financial Services | Protection, Wealth, Retirement, Legacy | Protection Gap Review page |
| Financial Literacy | Overview, Ages 8-13, 14-18, 19-25 | age-group landing pages (to be built) |
| Income Opportunities | Multiple Income, Advisor, Leader | **advisor readiness page** (built), leader page (to build) |
| Resources | 7 calculators/assessments, articles, videos, events | assessment → clarity call |
| For Organisations | Corporate / school / community workshops | enquiry form |
| Contact | Book a call | booking page |
| Legal | Privacy, Terms, Disclaimer | |

Homepage structure (from B): Hero → Why PLS → 3M model → 8 "Find your path" cards → Financial literacy → Silver/Gold/Diamond comparison → Learning ecosystem (16 modules) → Financial services → Retirement → Multiple income → Advisor → Leader → Masterclass → About Dr Maria → Why us → Organisations → Free tools → Final CTA.

Later "Community" layer (from C): Stories · Prosperity TV · Reads · Memberships · Masterclass registration · Join (member login needs a platform decision).

## 5. Reuse what is already built

| Existing file | Use on the new site |
|---|---|
| `prosperity-retirement-clarity-call.html` + booking pages | Retirement path destination |
| `prosperity-protection-gap-review.html` | Protection path destination |
| `prosperity-advisor-career-readiness.html` | Advisor path destination |
| `prosperity-clarity-call-v5.html` + thank-you | Clarity call funnel |
| Header, footer, logo, fonts, photo set | Shared design system for the main site |

Paid-ad landing pages stay **without the full main navigation**, as the brief says.

## 6. Phased build plan

| Phase | Duration | Work | Done when |
|---|---|---|---|
| 0. Decisions | week 1 | Answer section 2 and 3, choose platform, domain, CRM, booking tool, payment gateway. Get verified numbers, photos and the logo files | All open questions closed |
| 1. Design system + core pages | weeks 2-4 | Design tokens, header/footer, Home, About, Programs overview, Financial Planning, Financial Services, Financial Literacy overview, Income Opportunities, Resources, Contact | Phase 1 pages approved on mobile and desktop |
| 2. Program and service pages | weeks 4-7 | Silver, Gold, Diamond, Retirement hub, three youth age pages, Advisor, Leader, Protection, Corporate | Every CTA maps to a live destination |
| 3. Tools, SEO and content | weeks 7-11 | 7 calculators/assessments as indexable pages, article clusters (retirement first), videos/events library, schema, sitemap | Tools tested; first 8 articles live |
| 4. Community layer (optional) | weeks 10-14 | Masterclass registration, Join/Silver payment page, Stories, Prosperity TV, Reads, member login | Decision from section 2 row 1 |
| 5. QA and launch | week 12+ | Launch checklist from brief A section 18: forms, CRM source tracking, UTM, booking, payment links, speed, privacy pages, analytics events | Checklist signed off |

## 7. Platform and tracking

- **Platform (needs your decision):** WordPress with Elementor or Bricks is my recommendation: easy for the team to edit, strong for blog and SEO, handles forms and plugins. Member login, payments and TV/Stories (Phase 4) may need a membership plugin (e.g. a WordPress LMS/membership stack) or a separate platform.
- **CRM and forms:** one lead record with a **source field** (Retirement, Literacy, Advisor, Leader, Insurance, Webinar, Organic) plus UTM capture. Needs an approved CRM or database; Google Sheets works as a first step.
- **Analytics events:** form start, form submit, call booking, payment-page click, video play.
- **SEO:** hub-and-cluster. One strong page per intent, no thin duplicate pages. H1, title and meta on every page. Homepage H1 per brief: "Build Financial Clarity. Grow Wealth. Create a Prosperous Life."

## 8. Decisions I need from you

1. Build **hub site (A+B) first**, with the community pages (C) later? Or the other way round?
2. Final tier names and number (3 or 4)? Silver/Gold/Diamond (+Platinum)?
3. Colours and fonts: navy + gold + white with green accent, and Poppins?
4. Remove or keep the countdown, "seats left", hidden-offer timer? (I recommend removing.)
5. Verified numbers: 12,000+ / 500+ / 15+ vs 10,000+ families. Which is correct and provable?
6. Are ™ marks authorised?
7. Domain, hosting, CRM, booking tool and payment gateway: what already exists?
8. Who supplies logo files, photos, 9-12 success stories with permission, the book title, refund policy and payment links?

## 9. Immediate next steps once you answer

1. I build a **homepage design** (desktop + mobile) in the agreed palette.
2. Then the shared header/footer and Phase 1 pages as HTML, so you can approve the look before platform build-out.
