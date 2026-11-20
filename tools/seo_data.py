# -*- coding: utf-8 -*-
"""SEO content for every page: title, description, H1 keyword line, H2 changes, FAQs.
Keywords map = /KEYWORDS.md. Keep claims factual and promise-free."""

SITE = 'https://www.prosperitylifeschool.com'
BRAND = 'Prosperity Life School'
OG_IMAGE = SITE + '/assets/img/og-share.jpg'

# ------------------------------------------------------------------ main pages
MAIN = {
 'index.html': dict(
  title='Financial Planner in Bangalore | Prosperity Life School',
  desc='Financial planner in Bangalore and Mangalore for families in India and the Gulf. Retirement, insurance and wealth planning with Dr Maria Pramila Dsouza. Free call.',
  kw='Financial Planner in Bangalore &amp; Mangalore:',
  schema='home', crumb='Home',
  h2=[('Start Small. <em>Step It Up.</em> See the Difference.', 'SIP Step-Up Calculator: Start Small. <em>Step It Up.</em> See the Difference.'),
      ('Silver, Gold and Diamond: One Steady Path', 'Personal Finance Course Online: Silver, Gold and Diamond Membership'),
      ('Is Your Health Insurance <em>Really</em> Protecting You?', 'Is Your Health Insurance <em>Really</em> Protecting You? Check the Gaps')],
  faq_title='Financial Planning in Bangalore and Mangalore: Your Questions Answered',
  faq=[
   ('What does a financial planner in Bangalore do?',
    'A financial planner looks at your income, expenses, protection, investments, loans and goals together, instead of in pieces. At Prosperity Life School, Dr Maria Pramila Dsouza, a Chartered Wealth Manager, starts with a free 1-to-1 clarity call so you can see where you stand before deciding on any next step.'),
   ('Do you only work with people in Bangalore and Mangalore?',
    'No. Prosperity Life School is based in Bengaluru and Mangaluru and works online with individuals and families across India and the Gulf.'),
   ('Is the first call really free?',
    'Yes. The Prosperity Clarity Call is a free 1-to-1 conversation with no obligation. It is about understanding your situation, not selling you a product.'),
   ('What is a step-up SIP, and how does the calculator work?',
    'A step-up SIP raises your monthly investment by a set percentage each year. The calculator on this page shows an illustration using an assumed 12% yearly return. It is an example to help you think, not a promise of returns.'),
   ('How can I create multiple sources of income?',
    'Start by understanding your skills, time and goals. The Advisor Career Readiness check shows whether a finance career suits you, and the Diamond membership covers income themes in depth. Income varies by person and is never guaranteed.'),
   ('Is this investment advice?',
    'No. Prosperity Life School provides financial education. Nothing on this website is personalised investment, tax or legal advice or a promise of returns.')]),
 'about.html': dict(
  title='Dr Maria Pramila Dsouza | Chartered Wealth Manager India',
  desc='Meet Dr Maria Pramila Dsouza, Chartered Wealth Manager and financial coach in India. Founder of Prosperity Life School, guiding families in India and the Gulf.',
  kw='Chartered Wealth Manager &amp; Financial Coach in India:',
  schema='about', crumb='About',
  h2=[('Financial Education That Families Can Actually Use', 'Chartered Wealth Manager Who Teaches Money in Plain Language'),
      ('The 3M Model', 'The 3M Model: Mindset, Money Management and Multiple Sources of Income')],
  faq_title='About Dr Maria: Frequently Asked Questions',
  faq=[
   ('Who is Dr Maria Pramila Dsouza?',
    'Dr Maria Pramila Dsouza is a Chartered Wealth Manager, financial coach and the founder of Prosperity Life School. She began as a government school teacher, earned a PhD in Finance and now teaches families practical money skills.'),
   ('What does a financial coach do?',
    'A financial coach helps you understand your money, build better habits and make decisions that match your goals. Dr Maria combines education with practical implementation across money management, protection, investing, retirement and income creation.'),
   ('Which languages does Dr Maria teach in?',
    'English, Kannada, Tulu and Konkani. Her YouTube channel has videos in English and Kannada.'),
   ('Where does Dr Maria work with families?',
    'From Bengaluru and Mangaluru, and online with families across India and the Gulf, including NRI families.'),
   ('What is the GEM Framework?',
    'GEM stands for Grow Awareness, Elevate Wealth and Master Life Skills. It is the framework Dr Maria created for Prosperity Life School.'),
   ('How do I book a call with Dr Maria?',
    'Fill in the form on the Contact page and our team will confirm a time with you on WhatsApp or by phone. The first conversation is free.')]),
 'programs.html': dict(
  title='Personal Finance Course Online India: Programs & Membership',
  desc='Personal finance programs and Silver, Gold and Diamond membership from Prosperity Life School: clarity call, retirement, protection and advisor career.',
  kw='Personal Finance Course Online in India:',
  schema='programs', crumb='Programs',
  h2=[('Silver, Gold and Diamond: One Steady Path', 'Silver, Gold and Diamond Membership: One Steady Path')],
  faq_title='Programs and Membership: Frequently Asked Questions',
  faq=[
   ('What is the difference between Silver, Gold and Diamond?',
    'Silver (Prosperity Blueprint) builds your money foundation with 16 modules and live calls. Gold (Prosperity Navigator) gives you a personal financial plan with implementation guidance. Diamond (Prosperity Mastery) adds income skills and is by qualification.'),
   ('Is there a free way to start?',
    'Yes. You can join the free community and attend a free masterclass first. Paid memberships are optional.'),
   ('Why are website prices different from webinar prices?',
    'Webinar attendees receive a special lower price on their own registration page. The prices on this website are the standard website prices.'),
   ('How do I join Diamond?',
    'Diamond is offered on a qualification basis. Fill in the Diamond application form on this page and our team will review it and get back to you.'),
   ('Is this an online course I can do from anywhere?',
    'Yes. Programs and live calls are online, so families across India and the Gulf can join.'),
   ('Do the programs guarantee returns or income?',
    'No. Prosperity Life School provides education. Member results are individual and depend on their own effort and choices.')]),
 'community.html': dict(
  title='Financial Literacy Community India: Join Prosperity Community',
  desc='Join the Prosperity community for families in India and the Gulf. Free masterclass, live weekly mentor calls and 16 money-mastery modules with Dr Maria.',
  kw='Financial Literacy Community in India:',
  schema='community', crumb='Join Community',
  h2=[('A Community Built Around Action, Not Just Advice', 'A Financial Literacy Community Built Around Action, Not Just Advice')],
  faq_title=None, faq=None),   # page already has its own FAQ (kept as is, used for schema)
 'youtube.html': dict(
  title='Financial Literacy Videos in English & Kannada | Dr Maria',
  desc='Free financial literacy videos and money tips in English and Kannada from Dr Maria Pramila Dsouza: insurance, retirement, NRI tips, podcasts and Shorts.',
  kw='Financial Literacy Videos &amp; Money Tips on YouTube:',
  schema='youtube', crumb='YouTube',
  h2=[('Start With the Topic You Care About', 'Money Tips Playlists: Insurance, Retirement, NRI and Kannada Videos')],
  faq_title='Videos and Reels: Frequently Asked Questions',
  faq=[
   ('Where can I watch Dr Maria’s videos?',
    'On the YouTube channel Dr Maria’s Finance Chapel (@drmariapramila), and in short reels on Instagram (@drmariapramila).'),
   ('Are the videos free?',
    'Yes. All videos on YouTube are free to watch at any time.'),
   ('Are there videos in Kannada?',
    'Yes. Playlists such as Money Mathu and the Kannada financial literacy series are in Kannada, and many other videos are in English.'),
   ('What topics do the videos cover?',
    'Insurance explained, retirement, money mindset, podcasts and interviews, a book launch, live workshops and tips for NRIs.'),
   ('Are the examples in the reels a promise of returns?',
    'No. Illustrations in reels are examples only. The content is educational and not investment advice.')]),
 'contact.html': dict(
  title='Contact Prosperity Life School | Financial Planner Mangalore',
  desc='Contact Prosperity Life School and book a free call with Dr Maria Pramila Dsouza. Financial planner in Bangalore and Mangalore. WhatsApp +91 8904820166.',
  kw='Financial Planner in Mangalore &amp; Bangalore:',
  schema='contact', crumb='Contact',
  h2=[],
  faq_title='Contact and Booking: Frequently Asked Questions',
  faq=[
   ('How do I book a free call?',
    'Fill in the form on this page. Our team will confirm your slot on WhatsApp or by phone, usually within one or two working days.'),
   ('Is there a financial planner in Mangalore I can meet?',
    'Prosperity Life School works from Bengaluru and Mangaluru, and most conversations happen online so you can join from anywhere.'),
   ('What should I keep ready for the call?',
    'A broad view of your monthly income and expenses, existing investments and insurance, loans and your main goals. You never need to share passwords or OTPs.'),
   ('How can I reach you quickly?',
    'WhatsApp or call +91 8904820166, or email maria@prosperitylifeschool.com.')]),
}

# ------------------------------------------------------------------ landing pages
LANDING = {
 'prosperity-clarity-call-v5.html': dict(
  title='Free Financial Clarity Call | Financial Planning in India',
  desc='Book a free 1-to-1 financial clarity call with Dr Maria Pramila Dsouza, Chartered Wealth Manager. Financial planning for families, professionals and NRIs in India.',
  kicker=('\U0001F511 Prosperity Clarity Call', '\U0001F511 Free Financial Clarity Call · Financial Planning for Families in India'),
  crumb='Prosperity Clarity Call', service='Free financial clarity call and financial planning for families in India',
  h2=[('Frequently asked questions', 'Free Financial Clarity Call: Frequently Asked Questions')],
  faq=[('What is a free financial clarity call?',
        'It is a free 1-to-1 conversation with Dr Maria Pramila Dsouza where you look at your income, protection, investments, loans and goals together. It is about understanding your position, not selling a product.'),
       ('Is this financial planning for families in India only?',
        'The call is online, so families, professionals and NRIs in India and the Gulf can join.')]),
 'prosperity-retirement-clarity-call.html': dict(
  title='Retirement Planning India | Retirement Clarity Call with Dr Maria',
  desc='Retirement planning in India for professionals, families and NRIs. Book a free 1-to-1 Retirement Clarity Call with Chartered Wealth Manager Dr Maria Pramila Dsouza.',
  kicker=None, crumb='Retirement Clarity Call', service='Retirement planning clarity call for families and NRIs in India',
  h2=[('Different Retirement Stages Need Different Decisions', 'Retirement Planning India: Different Stages Need Different Decisions'),
      ('Frequently Asked Questions', 'Retirement Planning in India: Frequently Asked Questions')],
  faq=[('How much money do I need to retire in India?',
        'There is no single number. It depends on your expenses, age, dependents, inflation, health costs and existing assets. The Retirement Clarity Call helps you estimate your approximate needs and see how your current assets line up. Any figures shown are illustrations, not promises.'),
       ('Is retirement planning different for NRIs?',
        'NRIs often have assets, income and responsibilities in more than one country. The call helps organise that picture. Cross-border tax and legal matters should be handled with suitably qualified professionals.')]),
 'prosperity-protection-gap-review.html': dict(
  title='Insurance Gap Analysis | Free Protection Gap Review for Families',
  desc='Check your insurance gaps with a free 1-to-1 Protection Gap Review. Understand term insurance, health insurance waiting periods and room rent limits with Dr Maria.',
  kicker=None, crumb='Protection Gap Review', service='Insurance gap analysis and protection review for families in India',
  h2=[('Understand Your Protection Gap First', 'Insurance Gap Analysis: Understand Your Protection Gap First')],
  faq=[('How much term insurance do I need?',
        'There is no one-size rule. It depends on your income, liabilities, dependents, goals and existing cover. A good first step is to list what your family would need to stay financially secure, then compare it with the cover you already have.'),
       ('What are health insurance waiting periods and room rent limits?',
        'A waiting period is the time before certain conditions or treatments are covered. A room rent limit caps the daily room charge your policy pays for, and can reduce other claim payments if you choose a costlier room. Check the policy wording and ask the insurer in writing.'),
       ('What is an insurance gap analysis?',
        'It is a review that compares your life, health and accident cover with your responsibilities, so you can see where protection may be missing before you need it.')]),
 'prosperity-advisor-career-readiness.html': dict(
  title='Become a Financial Advisor in India | Career Readiness Scorecard',
  desc='Thinking of becoming a financial advisor in India? Take the Career Readiness Scorecard and book a free clarity call. Insurance advisor career guidance by Dr Maria.',
  kicker=None, crumb='Advisor Career Readiness', service='Financial advisor career readiness assessment and guidance in India',
  h2=[('Frequently Asked Questions', 'Become a Financial Advisor in India: Frequently Asked Questions'),
      ('Which Best Describes Your Current Situation?', 'Which Best Describes Your Current Situation? Start Your Advisor Career Check')],
  faq=[('How do I become a financial advisor in India?',
        'Requirements depend on the products you want to advise on, such as insurance or mutual funds, and each has its own certification and regulatory steps. The readiness scorecard helps you check your fit before you commit. Regulations change, so confirm current rules with the relevant regulator.'),
       ('Is an insurance advisor career a good option in India?',
        'It can suit people who enjoy teaching, building trust and long-term relationships. Income varies widely between individuals and is not guaranteed.'),
       ('How can I create multiple sources of income?',
        'Begin with your skills, time and goals. A finance advisory career is one pathway among several, and the clarity call helps you judge whether it deserves a closer look.')]),
 'book-retirement-clarity-call.html': dict(
  title='Retirement Planning India: What Happens on the Clarity Call',
  desc='See exactly what happens on your 1-to-1 Retirement Clarity Call with Dr Maria Pramila Dsouza. Retirement planning for NRIs and families in India.',
  kicker=None, crumb='Retirement Clarity Call: What Happens', service='1-to-1 retirement planning clarity call',
  h2=[('Frequently Asked Questions', 'Retirement Planning for NRIs and Families: Frequently Asked Questions')], faq=None),
 'retirement-booking-form.html': dict(
  title='Book Your Retirement Clarity Call | Prosperity Life School',
  desc='Book your free 1-to-1 Retirement Clarity Call with Dr Maria Pramila Dsouza. It takes about a minute.',
  kicker=None, crumb='Book Retirement Clarity Call', service=None, noindex=True, h2=[], faq=None),
 'prosperity-thank-you.html': dict(
  title='Thank You | Prosperity Life School',
  desc='Thank you for registering your 1-on-1 Prosperity Clarity Call.',
  kicker=None, crumb='Thank You', service=None, noindex=True, h2=[], faq=None),
}

PAGE_ORDER = ['index.html', 'about.html', 'programs.html', 'community.html', 'youtube.html', 'contact.html',
              'prosperity-clarity-call-v5.html', 'prosperity-retirement-clarity-call.html',
              'prosperity-protection-gap-review.html', 'prosperity-advisor-career-readiness.html',
              'book-retirement-clarity-call.html']
