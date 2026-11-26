# -*- coding: utf-8 -*-
"""ONE-TIME source edits (2026-11-26) from the client's 'All Links' document. Already applied; kept for the record."""
import re
W = '/home/user/prosperity/website/'
def rd(n): return open(W + n, encoding='utf8').read()
def wr(n, s): open(W + n, 'w', encoding='utf8').write(s)
def sub1(s, a, b):
    assert a in s, 'missing: ' + a[:70]
    return s.replace(a, b, 1)

SURVEY = 'https://clarity.prosperitylifeschool.com/survey2'
L = 'https://links.prosperitylifeschool.com/'
ext = 'target="_blank" rel="noopener"'

# ------------------------------------------------ programs: real membership options and links
s = rd('programs-multifile.html')
a, b = s.index('<div class="mem3">'), s.index('<p class="plat3">')
new = '''<div class="mem3">
<div class="mem"><span class="bd">Silver &middot; Foundation</span><h3>Prosperity Blueprint</h3><p class="d">Build your money foundation step by step, with courses, a 21-day money challenge, a weekly live call and a community of families.</p>
<ul><li>Courses and the 21-Day Money Manifestation Challenge (English, Kannada and Konkani)</li><li>Weekly Thursday Inner Circle call, 8 to 9 PM IST</li><li>Monthly 3-day bootcamp, 14 calculators and the Money Map toolkit</li></ul>
<div class="opt3">
<div class="op"><div><b>Silver &middot; 1 member</b><small>Full Silver for one person</small></div><div class="pr">&#8377;9,999<small>+ GST</small></div><a class="btn sm" href="%(L)sProsperityBlueprint-Silver" data-link="silver_individual" %(x)s>Join Silver</a></div>
<div class="op best"><span class="mc">Best for families</span><div><b>Silver &middot; 2 family members</b><small>Full payment for you and one family member</small></div><div class="pr">&#8377;12,999<small>incl. GST</small></div><a class="btn sm" href="%(L)ssilver-family" data-link="silver_family" %(x)s>Join as a Family</a></div>
<div class="op"><div><b>Family token booking</b><small>Pay &#8377;2,000 now to reserve. Total &#8377;14,999</small></div><div class="pr">&#8377;2,000<small>now</small></div><a class="btn sm" href="%(L)ssilver-family-token" data-link="silver_token" %(x)s>Reserve with &#8377;2,000</a></div>
</div>
<p class="web">Website price. <a href="%(L)splsk-offer-page" data-link="webinar_silver" %(x)s>Attended our webinar? Claim the webinar offer.</a></p>
<a class="pdf" href="%(L)spls-silver-membership" data-link="silver_page" %(x)s>See all Silver options</a>
<a class="pdf" href="#" data-link="onepager_silver" data-pdf hidden>Download the Silver one-pager (PDF)</a></div>
<div class="mem gl"><span class="bd">Gold &middot; Plan</span><h3>Prosperity Navigator</h3><p class="d">A personalised family financial plan built with our team, plus 6 months of support to put it into action. Includes Silver.</p>
<ul><li>Personalised family financial plan</li><li>6-month implementation support</li><li>Silver membership included</li></ul>
<a class="btn" href="%(L)sProsperityNavigator-Gold" data-link="gold" %(x)s>Join Gold</a>
<a class="pdf" href="#" data-link="onepager_gold" data-pdf hidden>Download the Gold one-pager (PDF)</a></div>
<div class="mem dia"><span class="bd">Diamond &middot; Earn</span><h3>Prosperity Mastery</h3><p class="d">A 1-year journey: Gold plus skills and multiple sources of income. <b>Diamond is by qualification:</b> apply and our team will review your application.</p>
<ul><li>Everything in Gold</li><li>Skills for multiple sources of income</li><li>Weekly Monday call with Dr Maria</li></ul>
<a class="btn" href="#diamond-apply">Apply for Diamond</a>
<a class="pdf" href="#" data-link="onepager_diamond" data-pdf hidden>Download the Diamond one-pager (PDF)</a></div>
</div>
''' % dict(L=L, x=ext)
s = s[:a] + new + s[b:]
wr('programs-multifile.html', s)

# ------------------------------------------------ home: SIP buttons + free tools section + masterclass link
s = rd('index-multifile.html')
s = sub1(s, 'Plan My SIP With Dr Maria <svg class="ic"><use href="#i-arrow"/></svg></a></div>',
         'Plan My SIP With Dr Maria <svg class="ic"><use href="#i-arrow"/></svg></a><a class="btn ghost lg" href="https://www.zfunds.in/visiting-card/d2bc55de-8cb0-4e97-a5ac-3b67a455505c" %s>Start a SIP or SWP</a></div>' % ext)
tools = '''<section class="bg-cream reveal" id="tools"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Free for everyone</span><h2>Free Tools and Assessments to Know Where You Stand</h2><p>Quick, plain-language check-ups for your family&#8217;s money. No jargon, no cost.</p></div>
<div class="ftgrid">
<a class="fta" href="%(S)s" %(x)s><span class="fi"><svg class="ic"><use href="#i-compass"/></svg></span><h3>Financial Clarity Assessment</h3><p>See where you stand today. Includes a free 1:1 clarity call.</p><span class="go">Start now <svg class="ic"><use href="#i-arrow"/></svg></span></a>
<a class="fta" href="https://calculator.prosperitylifeschool.com/" %(x)s><span class="fi"><svg class="ic"><use href="#i-calc"/></svg></span><h3>Family Money Check-ups</h3><p>9 quick check-ups in English and Kannada.</p><span class="go">Open check-ups <svg class="ic"><use href="#i-arrow"/></svg></span></a>
<a class="fta" href="https://calculator.prosperitylifeschool.com/pls-family-money/family-checkup" %(x)s><span class="fi"><svg class="ic"><use href="#i-plan"/></svg></span><h3>Family Financial Checkup</h3><p>Home loan, children&#8217;s education, retirement and life cover, with a score.</p><span class="go">Check my family <svg class="ic"><use href="#i-arrow"/></svg></span></a>
<a class="fta" href="%(L)sinsurance-assessment" %(x)s><span class="fi"><svg class="ic"><use href="#i-shield"/></svg></span><h3>Insurance Assessment</h3><p>See how well your insurance fits your family.</p><span class="go">Take the assessment <svg class="ic"><use href="#i-arrow"/></svg></span></a>
<a class="fta" href="%(L)spls-accins-assessment" %(x)s><span class="fi"><svg class="ic"><use href="#i-shield"/></svg></span><h3>Accidental Insurance Assessment</h3><p>Have health and life insurance but no accident cover? Check here.</p><span class="go">Take the assessment <svg class="ic"><use href="#i-arrow"/></svg></span></a>
<a class="fta" href="https://www.zfunds.in/visiting-card/d2bc55de-8cb0-4e97-a5ac-3b67a455505c" %(x)s><span class="fi"><svg class="ic"><use href="#i-trend"/></svg></span><h3>Start a SIP or SWP</h3><p>Enter your details, download our visiting card and contact us directly.</p><span class="go">Get started <svg class="ic"><use href="#i-arrow"/></svg></span></a>
</div>
<p class="fine" style="color:var(--ink-soft);text-align:center">Educational tools. Not investment advice or a promise of returns.</p>
</div></section>
''' % dict(S=SURVEY, L=L, x=ext)
marker = 'Start a SIP or SWP</a></div>\n</div>\n</div>\n</section>\n'
s = sub1(s, marker, marker + tools)
s = sub1(s, '<a class="btn ghost lg" href="community.html#join">Attend a Free Masterclass</a>',
         '<a class="btn ghost lg" href="https://landingpage.prosperitylifeschool.com/pls-kannada/" %s>Free Kannada Masterclass</a>' % ext)
wr('index-multifile.html', s)

# ------------------------------------------------ community
s = rd('community-multifile.html')
s = sub1(s, '<a class="btn ghost lg" href="community.html#join">Attend a Free Masterclass</a>',
         '<a class="btn ghost lg" href="https://landingpage.prosperitylifeschool.com/pls-kannada/" %s>Free Kannada Masterclass</a>' % ext)
s = sub1(s, '<h3>Join our WhatsApp group</h3><p>You will get a link to the community group and the next free masterclass.</p>',
         '<h3>Follow our WhatsApp Channel</h3><p>Get daily money content and the next free masterclass details on WhatsApp.</p>')
s = sub1(s, '<p>Answer two quick questions and we will send you the group link and the next free masterclass details on WhatsApp.</p>',
         '<p>Share your details and we will send you the next free masterclass details on WhatsApp.</p><div class="cta-row"><a class="btn wab" href="https://whatsapp.com/channel/0029Va7vp5iLo4hdA8ZQvC1c" %s><svg class="ic" style="fill:#fff;stroke:none"><use href="#b-wa"/></svg>Follow the WhatsApp Channel</a><a class="btn ghost" href="https://landingpage.prosperitylifeschool.com/pls-kannada/" %s>Register: Free Kannada Masterclass</a></div>' % (ext, ext))
s = sub1(s, 'You can start free by joining the WhatsApp group and attending', 'You can start free by following the WhatsApp Channel and attending')
s = s.replace('we will send you the community link and the next free masterclass details.', 'we will send you the community details and the next free masterclass details.')
wr('community-multifile.html', s)

# ------------------------------------------------ contact: office phone, calendar, enquiry forms
s = rd('contact-multifile.html')
s = sub1(s, '<div class="ci"><span class="ico"><svg class="ic"><use href="#i-mail"/></svg></span>',
         '<div class="ci"><span class="ico"><svg class="ic"><use href="#i-phone"/></svg></span><div><b>Office</b><a href="tel:+918073384729">+91 80733 84729</a></div></div>\n<div class="ci"><span class="ico"><svg class="ic"><use href="#i-mail"/></svg></span>')
enq = '''<section class="reveal" id="enquiry"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Prefer a specific option?</span><h2>Pick a Time or Make a Specific Enquiry</h2><p>Choose an exact time for your call, or ask about a particular need.</p></div>
<div class="ftgrid">
<a class="fta" href="%(L)s121calender" %(x)s><span class="fi"><svg class="ic"><use href="#i-chat"/></svg></span><h3>Book a 1:1 Call</h3><p>Pick the exact day and time that suits you.</p><span class="go">Open calendar <svg class="ic"><use href="#i-arrow"/></svg></span></a>
<a class="fta" href="%(L)sretirement-planning-form" %(x)s><span class="fi"><svg class="ic"><use href="#i-sun"/></svg></span><h3>Retirement Planning Enquiry</h3><p>Plan the years after work with clarity.</p><span class="go">Make an enquiry <svg class="ic"><use href="#i-arrow"/></svg></span></a>
<a class="fta" href="%(L)slife-insurance-form" %(x)s><span class="fi"><svg class="ic"><use href="#i-shield"/></svg></span><h3>Life Insurance Enquiry</h3><p>Protect your family&#8217;s future income.</p><span class="go">Make an enquiry <svg class="ic"><use href="#i-arrow"/></svg></span></a>
<a class="fta" href="%(L)shealth-insurance-form" %(x)s><span class="fi"><svg class="ic"><use href="#i-shield"/></svg></span><h3>Health Insurance Enquiry</h3><p>Understand cover, waiting periods and limits.</p><span class="go">Make an enquiry <svg class="ic"><use href="#i-arrow"/></svg></span></a>
<a class="fta" href="%(L)saccidental-insurance-form" %(x)s><span class="fi"><svg class="ic"><use href="#i-shield"/></svg></span><h3>Personal Accident Insurance Enquiry</h3><p>Cover for the unexpected.</p><span class="go">Make an enquiry <svg class="ic"><use href="#i-arrow"/></svg></span></a>
<a class="fta" href="%(L)sbusiness-insurance-form" %(x)s><span class="fi"><svg class="ic"><use href="#i-brief"/></svg></span><h3>Business Insurance Enquiry</h3><p>Protect your business and your people.</p><span class="go">Make an enquiry <svg class="ic"><use href="#i-arrow"/></svg></span></a>
</div></div></section>

''' % dict(L=L, x=ext)
s = sub1(s, '<section class="bg-cream reveal" id="legal">', enq + '<section class="bg-cream reveal" id="legal">')
wr('contact-multifile.html', s)

# ------------------------------------------------ youtube: three channels
s = rd('youtube-multifile.html')
ch = '''<section class="reveal" id="channels"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Three channels</span><h2>Choose Your Channel and Language</h2><p>Subscribe to the one that suits you, or all three.</p></div>
<div class="ftgrid">
<a class="fta" href="https://www.youtube.com/@SamriddhiwithDrMaria?sub_confirmation=1" %(x)s><span class="fi yt"><svg class="ic" style="fill:#fff;stroke:none"><use href="#b-yt"/></svg></span><h3>Samriddhi with Dr. Maria</h3><p>Kannada &middot; money lessons in your language.</p><span class="go">Subscribe <svg class="ic"><use href="#i-arrow"/></svg></span></a>
<a class="fta" href="https://www.youtube.com/@prosperitylifeschool?sub_confirmation=1" %(x)s><span class="fi yt"><svg class="ic" style="fill:#fff;stroke:none"><use href="#b-yt"/></svg></span><h3>Prosperity Life School</h3><p>English &middot; programs, masterclasses and member lessons.</p><span class="go">Subscribe <svg class="ic"><use href="#i-arrow"/></svg></span></a>
<a class="fta" href="https://www.youtube.com/@drmariapramila?sub_confirmation=1" %(x)s><span class="fi yt"><svg class="ic" style="fill:#fff;stroke:none"><use href="#b-yt"/></svg></span><h3>Dr Maria&#8217;s Finance Chapel</h3><p>English &middot; 500+ videos on insurance, retirement, mindset and NRI tips.</p><span class="go">Subscribe <svg class="ic"><use href="#i-arrow"/></svg></span></a>
</div></div></section>

''' % dict(x=ext)
s = sub1(s, '<section class="bg-cream reveal" id="playlists">', ch + '<section class="bg-cream reveal" id="playlists">')
wr('youtube-multifile.html', s)
print('sources updated')
