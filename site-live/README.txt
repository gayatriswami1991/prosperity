Prosperity Life School: LIVE website (www.prosperitylifeschool.com)

UPLOAD: put ALL files and the assets/ folder (and .htaccess, which is hidden) in the root of the website (public_html).
Pages (13): index, about, programs, community, youtube, contact + 4 ad landing pages + book-retirement-clarity-call,
retirement-booking-form, prosperity-thank-you. Extra: sitemap.xml, robots.txt, .htaccess (https + www redirect, cache).

FORM: every page uses the same Umang Digital form (iframe). To change it, edit FORM_URL in tools/build.py and rebuild.
LINKS: membership / PDF links live in assets/js/site.js (PSL_CONFIG.LINKS). Empty = button goes to the Contact page.
AFTER GO-LIVE: submit https://www.prosperitylifeschool.com/sitemap.xml in Google Search Console.
Rebuild:  python3 tools/build.py  then  python3 tools/validate.py
