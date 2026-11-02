# Prosperity Life School: Full Website Roadmap (v3)

Source: the three client documents (Developer Instructions, Website Content 1, Website Content). I resolved the conflicts myself using the documents and the logo. Everything marked **CONFIRM** goes to the client once, in one go.

## 1. Decisions made (from the documents)

| Topic | Decision | Why |
|---|---|---|
| Site concept | **One website**: hub site (Developer Instructions + Content 1) with the community pages from Content (Masterclass, Stories, TV, Reads, Memberships) placed inside it | Both documents come from the client; the hub brief is the master, the community pages are added as sections |
| Navigation | The 9 items from the Developer brief. Community pages sit under Programs (Masterclass, tiers) and Resources (TV, Reads, Stories under About) | Keeps the brief's menu, loses nothing |
| Primary CTA | **Take Free Assessment** (header, hero, final). Secondary: Explore Programs / Free Masterclass | The brief says so |
| Tiers | Silver = Prosperity Blueprint, Gold = Prosperity Navigator, Diamond = Prosperity Mastery (3-card comparison) + **Platinum Circle (invite only)** as a strip below | Content 1 names three tiers with product names; Content adds Platinum |
| Numbers | **12,000+ people educated, 500+ client families, 15+ years** | Appear in Content 1 and in every earlier document. Content says "10,000+ families guided": **CONFIRM** which is right |
| Fonts | **Poppins** | The brief names Poppins or Arial |
| Logo | Exact supplied logo, not redrawn | Brief |
| ™ marks | Not used on the main site | Brief says no ™ unless authorised |

## 2. Colours (chosen from the logo and the business)

I sampled the logo: it is **navy `#011D44` and gold/bronze**, with no green in it. Finance + education + "prosperity" also points to navy (trust) and gold (wealth).

| Role | Colour |
|---|---|
| Primary (trust) | Navy `#011D43`, deep navy `#001330`, blue `#123A73` for gradients |
| Accent (prosperity) | Gold `#D09C32`, bright gold `#E8BC5A`, deep gold `#8F6A17` for text on white |
| Surfaces | White, cream `#FBF8F1`, mist `#F2F5FA`, gold tint `#FBF1DA` |
| Tick marks only | Soft green `#1F8A63` (so the brief's "green" is still honoured, used sparingly) |

Content (the 7-page document) specifies exactly navy `#011D43` and gold `#D09C32`, so this matches it. Landing pages already built keep their own palette for ad campaigns.

## 3. Claims in the documents (kept, flagged for client confirmation)

| Claim | Where it is in the documents | Status in the build |
|---|---|---|
| 15+ years, 12,000+ educated, 500+ client families | Content 1 (About), earlier docs | Used. Needs proof on file |
| 10,000+ families guided; [X]+ Trustpilot reviews; Hall of Fame count; ₹ crore invested by members | Content, as bracketed placeholders | **Not published**. Left out until real numbers arrive |
| "₹52 lakh in 9 months" (Diamond member) | Content, success story card | Shown with the member name and permission as placeholders. **CONFIRM** it is true and permitted |
| "I am at peace." (Gold member) | Content | Shown as placeholder |
| "Earn your first extra ₹1 lakh a month" (Diamond) | Content | **Not used** on the home page: an income claim |
| "PhD in Finance, Chartered Wealth Manager", GEM Framework, teaches English/Kannada/Tulu/Konkani, guides families in India and the Gulf | Content | Used in the About block |
| Masterclass "₹999 value, FREE", "₹1,999 FREE", countdown, seats left, 5-minute timer | Content | **Not used**. Countdown and hidden-offer timer remain off |
| Silver prices Rs 7,999 / 9,999 / 13,999 | Content (Join page) | Reserved for the Join page. **CONFIRM** public pricing |
| Disclaimer text | Content and Content 1 | Used in the footer |

## 4. Pages: what gets built and what each one contains

Legend: **LIVE** = already built (landing page), **NEW** = to build.

### Home (`index.html`, built)
Header + top bar → Hero (H1 "Build Financial Clarity. Grow Wealth. Create a Prosperous Life.", 2 CTAs, keyword chips, Dr Maria photo, 4-number proof strip) → Why Prosperity Life School (8 gaps) → 3M Model → "Find your path" (8 cards) → Financial literacy (3 age cards) → Silver / Gold / Diamond + Platinum strip → 16-module ecosystem → Financial services (4 columns + disclaimer) → Retirement + Multiple income → Advisor + Leadership → Free Masterclass → About Dr Maria → Education / Clarity / Implementation / Accountability → Success stories → Prosperity TV + Reads → For Organisations → 7 Free Tools → Final CTA → Footer (contact, legal, disclaimer, WhatsApp, sticky mobile CTA).

### About
| Page | Contents |
|---|---|
| About Dr Maria (`about.html`) | Journey from government teacher to wealth mentor, credentials, GEM Framework, languages, photo set, video, CTA |
| About PLS (`about-pls.html`) | Mission, 3M model, Education→Clarity→Implementation→Accountability, ecosystem diagram, team |
| Success Stories (`stories.html`) | Story feed, newest first; each card: category, membership badge, read time, title, name, result. Six stages Spark→Fall→Shift→Climb→Rise→Ripple. "Write your story" for members |

### Programs
| Page | Contents |
|---|---|
| Programs overview | 4 tiers as a path, comparison, which step fits you, FAQs |
| Silver · Prosperity Blueprint | 16 modules, live weekly calls, community. Join options (Individual / Plus / Family) after confirmation of prices |
| Gold · Prosperity Navigator | Personal financial plan, implementation guidance, 6-month review, process, FAQs |
| Diamond · Prosperity Mastery | Certification, Monday calls, 12 income themes, waitlist form |
| Platinum Circle | Invite-only, retreats, application form |
| Free Masterclass (`masterclass.html`) | English and Kannada versions: hero, 3M secrets, who it is for, bonuses, mentor, FAQ, registration form. No fake countdown |
| Workshops | Public workshops and events |

### Financial Planning
| Page | Contents |
|---|---|
| Overview | The three paths below + assessment CTA |
| Financial Clarity | **LIVE** `prosperity-clarity-call-v5.html` |
| Comprehensive Financial Planning | NEW: cash flow, emergency fund, debt, protection, investments, goals, retirement, tax, succession; process; CTA |
| Retirement Planning | **LIVE** `prosperity-retirement-clarity-call.html` + booking pages; NEW hub page with the 4 stages, calculator and blog links |

### Financial Services
| Page | Contents |
|---|---|
| Overview | 4 service groups + product disclaimer |
| Protection | **LIVE** `prosperity-protection-gap-review.html` |
| Wealth Creation | NEW: mutual funds, SIPs, goal-based planning |
| Retirement | NEW: corpus strategy, income planning, withdrawal strategies |
| Wealth & Legacy | NEW: portfolio planning, succession |

### Financial Literacy
Overview, Ages 8-13 Money Foundations, Ages 14-18 Young Money Skills, Ages 19-25 Financial Independence. Each: curriculum, how sessions run, parent FAQ, enrol / enquiry form.

### Income Opportunities
| Page | Contents |
|---|---|
| Multiple Sources of Income | 9 pathways, "identify the right opportunities", income planner CTA |
| Become an Advisor | **LIVE** `prosperity-advisor-career-readiness.html` |
| Leadership Opportunity | NEW: recruit, train, mentor, build systems, grow a business |

### Resources
Free Tools hub + **7 indexable tool pages** (Insurance Gap, Cash Flow, Debt Health, Retirement Number, Risk Appetite, Protection Knowledge, Multiple Income Planner), each with explanation, tool, interpretation, related content, CTA · Articles/Blog (hub-and-cluster) · Prosperity TV (shows, filters, featured talk) · Prosperity Reads (books, free preview, reviews) · Events and webinars.

### Other
Assessment (Financial Clarity Assessment: short capture, then branching questions) · Contact / Book a Call (form, WhatsApp, email) · Corporate / School workshops · Privacy, Terms, Disclaimer · 404 page.

## 5. Header and footer (shared on every page)
Header: logo, 9-item navigation with dropdowns, **Take Free Assessment** button, optional **Book a Call**, mobile burger menu. Footer: short description, Programs, Financial Services, Learn & Grow, Contact (+91 8904820166, maria@prosperitylifeschool.com), social, Privacy Policy, Terms, Disclaimer, copyright 2026, disclaimer text.

## 6. Build phases
| Phase | Work |
|---|---|
| 1 | Home (done), About, Programs overview, Financial Planning, Financial Services, Financial Literacy overview, Income Opportunities, Resources, Contact |
| 2 | Silver, Gold, Diamond, Platinum, Masterclass, Retirement hub, three youth pages, Leadership, Corporate, Stories |
| 3 | 7 tool pages, blog clusters (retirement first), TV, Reads, events, CRM/UTM wiring |
| 4 | QA (mobile, speed, forms, links), SEO (titles, meta, schema, sitemap), launch checklist |

## 7. Technical
Static HTML + shared CSS/JS now (`website/`), ready to move into WordPress or any host. Poppins, mobile-first, lazy-loaded images, schema.org Organization data, one H1 per page, FAQ pages with FAQ schema, UTM capture and a source field on every form, analytics events for form start/submit, booking click and payment click.

## 8. One-time client confirmation list
1. 12,000+ / 500+ / 15+ versus 10,000+ families guided: which is correct and provable?
2. Are "₹52 lakh in 9 months" and the two success quotes real, with permission?
3. Silver prices public, or after the call?
4. Masterclass date/time (English and Kannada), seat and countdown policy (recommend none).
5. Book title and description; testimonials, photos, logo files; refund policy; payment links.
6. Social links, Trustpilot link, Google Form / CRM / booking tool.
