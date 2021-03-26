import os
import sys

import django

sys.path.append(".")  # noqa
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  # noqa
django.setup()  # noqa

from datetime import timedelta
from random import randint, random

from django.contrib.auth.models import User

from sis.models import Major, Semester, SemesterStudent, Student

to_generate = 1000

set_pass = True

specs = (
    ('tsowell', 'Thomas', 'Sowell', 'tsowell@x.com'),
    ('edouglas', 'Ellia', 'Douglas', 'e.douglas@x.com'),
    ('bcameron', 'Brianna', 'Cameron', 'b.cameron@x.com'),
    ('mfoster', 'Maddie', 'Foster', 'm.foster@x.com'),
    ('tperry', 'Tyler', 'Perry', 't.perry@x.com'),
    ('arogers', 'Aston', 'Rogers', 'a.rogers@x.com'),
    ('acarter', 'Adrian', 'Carter', 'a.carter@x.com'),
    ('phamilto', 'Penelope', 'Hamilton', 'p.hamilton@x.com'),
    ('rclark', 'Rubie', 'Clark', 'r.clark@x.com'),
    ('kevans', 'Kristian', 'Evans', 'k.evans@x.com'),
    ('lhall', 'Lydia', 'Hall', 'l.hall@x.com'),
    ('lroberts', 'Lily', 'Roberts', 'l.roberts@x.com'),
    ('nedwards', 'Nicole', 'Edwards', 'n.edwards@x.com'),
    ('hmurray', 'Harold', 'Murray', 'h.murray@x.com'),
    ('fwells', 'Frederick', 'Wells', 'f.wells@x.com'),
    ('amartin', 'Amanda', 'Martin', 'a.martin@x.com'),
    ('aryan', 'Arthur', 'Ryan', 'a.ryan@x.com'),
    ('mwilliam', 'Maya', 'Williams', 'm.williams@x.com'),
    ('kholmes', 'Kristian', 'Holmes', 'k.holmes@x.com'),
    ('pperry', 'Paul', 'Perry', 'p.perry@x.com'),
    ('lriley', 'Lenny', 'Riley', 'l.riley@x.com'),
    ('jpayne', 'Jasmine', 'Payne', 'j.payne@x.com'),
    ('dturner', 'David', 'Turner', 'd.turner@x.com'),
    ('jedwards', 'Jasmine', 'Edwards', 'j.edwards@x.com'),
    ('rlloyd', 'Robert', 'Lloyd', 'r.lloyd@x.com'),
    ('atucker', 'Amy', 'Tucker', 'a.tucker@x.com'),
    ('emiller', 'Eric', 'Miller', 'e.miller@x.com'),
    ('vmorgan', 'Valeria', 'Morgan', 'v.morgan@x.com'),
    ('ncampbel', 'Nicholas', 'Campbell', 'n.campbell@x.com'),
    ('estewart', 'Emily', 'Stewart', 'e.stewart@x.com'),
    ('cdixon', 'Chester', 'Dixon', 'c.dixon@x.com'),
    ('sclark', 'Stella', 'Clark', 's.clark@x.com'),
    ('dwells', 'Daisy', 'Wells', 'd.wells@x.com'),
    ('ggrant', 'George', 'Grant', 'g.grant@x.com'),
    ('fdavis', 'Fiona', 'Davis', 'f.davis@x.com'),
    ('awells', 'Aldus', 'Wells', 'a.wells@x.com'),
    ('aowens', 'Alan', 'Owens', 'a.owens@x.com'),
    ('jcole', 'Jasmine', 'Cole', 'j.cole@x.com'),
    ('awalker', 'Alan', 'Walker', 'a.walker@x.com'),
    ('scameron', 'Stella', 'Cameron', 's.cameron@x.com'),
    ('hchapman', 'Harold', 'Chapman', 'h.chapman@x.com'),
    ('fhawkins', 'Frederick', 'Hawkins', 'f.hawkins@x.com'),
    ('olloyd', 'Oliver', 'Lloyd', 'o.lloyd@x.com'),
    ('rsmith', 'Rafael', 'Smith', 'r.smith@x.com'),
    ('fthompso', 'Florrie', 'Thompson', 'f.thompson@x.com'),
    ('aharris', 'Alfred', 'Harris', 'a.harris@x.com'),
    ('ejones', 'Emma', 'Jones', 'e.jones@x.com'),
    ('ariley', 'Alford', 'Riley', 'a.riley@x.com'),
    ('scooper', 'Steven', 'Cooper', 's.cooper@x.com'),
    ('dscott', 'Dale', 'Scott', 'd.scott@x.com'),
    ('khoward', 'Kellan', 'Howard', 'k.howard@x.com'),
    ('vharper', 'Violet', 'Harper', 'v.harper@x.com'),
    ('mscott', 'Maya', 'Scott', 'm.scott@x.com'),
    ('mrichard', 'Max', 'Richardson', 'm.richardson@x.com'),
    ('vfoster', 'Vanessa', 'Foster', 'v.foster@x.com'),
    ('cnelson', 'Clark', 'Nelson', 'c.nelson@x.com'),
    ('dhall', 'Dominik', 'Hall', 'd.hall@x.com'),
    ('vdavis', 'Vanessa', 'Davis', 'v.davis@x.com'),
    ('sowens', 'Sydney', 'Owens', 's.owens@x.com'),
    ('ebrooks', 'Edward', 'Brooks', 'e.brooks@x.com'),
    ('sscott', 'Sabrina', 'Scott', 's.scott@x.com'),
    ('wharper', 'Wilson', 'Harper', 'w.harper@x.com'),
    ('randerso', 'Rubie', 'Anderson', 'r.anderson@x.com'),
    ('khunt', 'Kelsey', 'Hunt', 'k.hunt@x.com'),
    ('lhawkins', 'Lucy', 'Hawkins', 'l.hawkins@x.com'),
    ('ecraig', 'Edgar', 'Craig', 'e.craig@x.com'),
    ('kmurphy', 'Kimberly', 'Murphy', 'k.murphy@x.com'),
    ('hwright', 'Haris', 'Wright', 'h.wright@x.com'),
    ('apayne', 'Alina', 'Payne', 'a.payne@x.com'),
    ('gwarren', 'Garry', 'Warren', 'g.warren@x.com'),
    ('chenders', 'Chester', 'Henderson', 'c.henderson@x.com'),
    ('gallen', 'Gianna', 'Allen', 'g.allen@x.com'),
    ('acrawfor', 'Arthur', 'Crawford', 'a.crawford@x.com'),
    ('nhenders', 'Natalie', 'Henderson', 'n.henderson@x.com'),
    ('lwalker', 'Luke', 'Walker', 'l.walker@x.com'),
    ('lmurphy', 'Luke', 'Murphy', 'l.murphy@x.com'),
    ('dkelly', 'Derek', 'Kelly', 'd.kelly@x.com'),
    ('jevans', 'Jacob', 'Evans', 'j.evans@x.com'),
    ('lrussell', 'Lana', 'Russell', 'l.russell@x.com'),
    ('rbarnes', 'Roman', 'Barnes', 'r.barnes@x.com'),
    ('wtucker', 'William', 'Tucker', 'w.tucker@x.com'),
    ('sbaker', 'Sam', 'Baker', 's.baker@x.com'),
    ('sriley', 'Sam', 'Riley', 's.riley@x.com'),
    ('lrobinso', 'Lily', 'Robinson', 'l.robinson@x.com'),
    ('arussell', 'Arianna', 'Russell', 'a.russell@x.com'),
    ('jcraig', 'Joyce', 'Craig', 'j.craig@x.com'),
    ('ewells', 'Eleanor', 'Wells', 'e.wells@x.com'),
    ('mcooper', 'Maria', 'Cooper', 'm.cooper@x.com'),
    ('agray', 'Arthur', 'Gray', 'a.gray@x.com'),
    ('sbrooks', 'Sarah', 'Brooks', 's.brooks@x.com'),
    ('farmstro', 'Freddie', 'Armstrong', 'f.armstrong@x.com'),
    ('sbrown', 'Sabrina', 'Brown', 's.brown@x.com'),
    ('nwilliam', 'Naomi', 'Williams', 'n.williams@x.com'),
    ('mharriso', 'Max', 'Harrison', 'm.harrison@x.com'),
    ('aalexand', 'Antony', 'Alexander', 'a.alexander@x.com'),
    ('obennett', 'Oliver', 'Bennett', 'o.bennett@x.com'),
    ('lchapman', 'Lilianna', 'Chapman', 'l.chapman@x.com'),
    ('tsmith', 'Tony', 'Smith', 't.smith@x.com'),
    ('kfarrell', 'Kelvin', 'Farrell', 'k.farrell@x.com'),
    ('mross', 'Maria', 'Ross', 'm.ross@x.com'),
    ('ewalker', 'Edith', 'Walker', 'e.walker@x.com'),
    ('tdouglas', 'Ted', 'Douglas', 't.douglas@x.com'),
    ('fwest', 'Fiona', 'West', 'f.west@x.com'),
    ('irichard', 'Isabella', 'Richards', 'i.richards@x.com'),
    ('sferguso', 'Sawyer', 'Ferguson', 's.ferguson@x.com'),
    ('jjohnsto', 'Jordan', 'Johnston', 'j.johnston@x.com'),
    ('nspencer', 'Naomi', 'Spencer', 'n.spencer@x.com'),
    ('badams', 'Brooke', 'Adams', 'b.adams@x.com'),
    ('mmartin', 'Miranda', 'Martin', 'm.martin@x.com'),
    ('nturner', 'Nicole', 'Turner', 'n.turner@x.com'),
    ('dtucker', 'Daryl', 'Tucker', 'd.tucker@x.com'),
    ('dstevens', 'Daryl', 'Stevens', 'd.stevens@x.com'),
    ('enelson', 'Eric', 'Nelson', 'e.nelson@x.com'),
    ('rmontgom', 'Rebecca', 'Montgomery', 'r.montgomery@x.com'),
    ('awilliam', 'Ashton', 'Williams', 'a.williams@x.com'),
    ('arichard', 'Alina', 'Richards', 'a.richards@x.com'),
    ('jwilson', 'Jasmine', 'Wilson', 'j.wilson@x.com'),
    ('aharper', 'Adrianna', 'Harper', 'a.harper@x.com'),
    ('bhenders', 'Belinda', 'Henderson', 'b.henderson@x.com'),
    ('mmurphy', 'Maximilian', 'Murphy', 'm.murphy@x.com'),
    ('acunning', 'Audrey', 'Cunningham', 'a.cunningham@x.com'),
    ('jhoward', 'Justin', 'Howard', 'j.howard@x.com'),
    ('aclark', 'Alina', 'Clark', 'a.clark@x.com'),
    ('pryan', 'Penelope', 'Ryan', 'p.ryan@x.com'),
    ('jhenders', 'Jasmine', 'Henderson', 'j.henderson@x.com'),
    ('pedwards', 'Patrick', 'Edwards', 'p.edwards@x.com'),
    ('obaker', 'Oliver', 'Baker', 'o.baker@x.com'),
    ('oanderso', 'Oliver', 'Anderson', 'o.anderson@x.com'),
    ('ajones', 'Arianna', 'Jones', 'a.jones@x.com'),
    ('dwilliam', 'Dominik', 'Williams', 'd.williams@x.com'),
    ('jspencer', 'Julian', 'Spencer', 'j.spencer@x.com'),
    ('dmorris', 'Darcy', 'Morris', 'd.morris@x.com'),
    ('powens', 'Patrick', 'Owens', 'p.owens@x.com'),
    ('bdouglas', 'Briony', 'Douglas', 'b.douglas@x.com'),
    ('cwright', 'Cherry', 'Wright', 'c.wright@x.com'),
    ('oroberts', 'Oliver', 'Roberts', 'o.roberts@x.com'),
    ('lmyers', 'Lilianna', 'Myers', 'l.myers@x.com'),
    ('thamilto', 'Ted', 'Hamilton', 't.hamilton@x.com'),
    ('vwalker', 'Violet', 'Walker', 'v.walker@x.com'),
    ('amurphy', 'Alissa', 'Murphy', 'a.murphy@x.com'),
    ('cfoster', 'Carl', 'Foster', 'c.foster@x.com'),
    ('mchapman', 'Melissa', 'Chapman', 'm.chapman@x.com'),
    ('pmitchel', 'Paige', 'Mitchell', 'p.mitchell@x.com'),
    ('ecole', 'Edwin', 'Cole', 'e.cole@x.com'),
    ('jroberts', 'Jenna', 'Roberts', 'j.roberts@x.com'),
    ('callen', 'Clark', 'Allen', 'c.allen@x.com'),
    ('amorgan', 'Alfred', 'Morgan', 'a.morgan@x.com'),
    ('jryan', 'Joyce', 'Ryan', 'j.ryan@x.com'),
    ('mstewart', 'Mike', 'Stewart', 'm.stewart@x.com'),
    ('levans', 'Lucas', 'Evans', 'l.evans@x.com'),
    ('crussell', 'Carlos', 'Russell', 'c.russell@x.com'),
    ('candrews', 'Cherry', 'Andrews', 'c.andrews@x.com'),
    ('wryan', 'Wilson', 'Ryan', 'w.ryan@x.com'),
    ('ecunning', 'Eddy', 'Cunningham', 'e.cunningham@x.com'),
    ('otaylor', 'Oscar', 'Taylor', 'o.taylor@x.com'),
    ('brichard', 'Brad', 'Richards', 'b.richards@x.com'),
    ('eallen', 'Elise', 'Allen', 'e.allen@x.com'),
    ('scunning', 'Sofia', 'Cunningham', 's.cunningham@x.com'),
    ('cwest', 'Clark', 'West', 'c.west@x.com'),
    ('hbrown', 'Harold', 'Brown', 'h.brown@x.com'),
    ('hbarnes', 'Honey', 'Barnes', 'h.barnes@x.com'),
    ('bwilliam', 'Bruce', 'Williams', 'b.williams@x.com'),
    ('lmitchel', 'Lucy', 'Mitchell', 'l.mitchell@x.com'),
    ('ledwards', 'Lily', 'Edwards', 'l.edwards@x.com'),
    ('ffarrell', 'Frederick', 'Farrell', 'f.farrell@x.com'),
    ('cscott', 'Cherry', 'Scott', 'c.scott@x.com'),
    ('fbrown', 'Frederick', 'Brown', 'f.brown@x.com'),
    ('emontgom', 'Elise', 'Montgomery', 'e.montgomery@x.com'),
    ('amoore', 'Alen', 'Moore', 'a.moore@x.com'),
    ('jjohnson', 'Jordan', 'Johnson', 'j.johnson@x.com'),
    ('cmorgan', 'Catherine', 'Morgan', 'c.morgan@x.com'),
    ('twright', 'Tyler', 'Wright', 't.wright@x.com'),
    ('cmason', 'Carl', 'Mason', 'c.mason@x.com'),
    ('fcooper', 'Frederick', 'Cooper', 'f.cooper@x.com'),
    ('lmiller', 'Lucy', 'Miller', 'l.miller@x.com'),
    ('ajohnson', 'Alissa', 'Johnson', 'a.johnson@x.com'),
    ('srussell', 'Savana', 'Russell', 's.russell@x.com'),
    ('dbarnes', 'Dominik', 'Barnes', 'd.barnes@x.com'),
    ('bmiller', 'Bruce', 'Miller', 'b.miller@x.com'),
    ('scarter', 'Savana', 'Carter', 's.carter@x.com'),
    ('mbailey', 'Maddie', 'Bailey', 'm.bailey@x.com'),
    ('anelson', 'Alberta', 'Nelson', 'a.nelson@x.com'),
    ('tclark', 'Tess', 'Clark', 't.clark@x.com'),
    ('bjohnson', 'Briony', 'Johnson', 'b.johnson@x.com'),
    ('dmorgan', 'Dexter', 'Morgan', 'd.morgan@x.com'),
    ('dmurphy', 'Darcy', 'Murphy', 'd.murphy@x.com'),
    ('acampbel', 'Agata', 'Campbell', 'a.campbell@x.com'),
    ('lalexand', 'Luke', 'Alexander', 'l.alexander@x.com'),
    ('rriley', 'Roland', 'Riley', 'r.riley@x.com'),
    ('aevans', 'Aston', 'Evans', 'a.evans@x.com'),
    ('mlloyd', 'Mike', 'Lloyd', 'm.lloyd@x.com'),
    ('ahenders', 'Alexander', 'Henderson', 'a.henderson@x.com'),
    ('amorris', 'Amelia', 'Morris', 'a.morris@x.com'),
    ('eperkins', 'Elian', 'Perkins', 'e.perkins@x.com'),
    ('ecooper', 'Elise', 'Cooper', 'e.cooper@x.com'),
    ('rturner', 'Rafael', 'Turner', 'r.turner@x.com'),
    ('jthompso', 'Jenna', 'Thompson', 'j.thompson@x.com'),
    ('jwalker', 'Jack', 'Walker', 'j.walker@x.com'),
    ('mhall', 'Marcus', 'Hall', 'm.hall@x.com'),
    ('cbrooks', 'Charlie', 'Brooks', 'c.brooks@x.com'),
    ('kadams', 'Kevin', 'Adams', 'k.adams@x.com'),
    ('oriley', 'Olivia', 'Riley', 'o.riley@x.com'),
    ('pfoster', 'Penelope', 'Foster', 'p.foster@x.com'),
    ('cross', 'Chloe', 'Ross', 'c.ross@x.com'),
    ('nstevens', 'Natalie', 'Stevens', 'n.stevens@x.com'),
    ('rjones', 'Ryan', 'Jones', 'r.jones@x.com'),
    ('dcooper', 'Daryl', 'Cooper', 'd.cooper@x.com'),
    ('mmyers', 'Myra', 'Myers', 'm.myers@x.com'),
    ('rwatson', 'Richard', 'Watson', 'r.watson@x.com'),
    ('mmoore', 'Martin', 'Moore', 'm.moore@x.com'),
    ('acole', 'Aiden', 'Cole', 'a.cole@x.com'),
    ('rscott', 'Roland', 'Scott', 'r.scott@x.com'),
    ('nwells', 'Natalie', 'Wells', 'n.wells@x.com'),
    ('kbarnes', 'Kelsey', 'Barnes', 'k.barnes@x.com'),
    ('abrooks', 'Ashton', 'Brooks', 'a.brooks@x.com'),
    ('khamilto', 'Kevin', 'Hamilton', 'k.hamilton@x.com'),
    ('cwilson', 'Chloe', 'Wilson', 'c.wilson@x.com'),
    ('tturner', 'Ted', 'Turner', 't.turner@x.com'),
    ('sturner', 'Savana', 'Turner', 's.turner@x.com'),
    ('akelley', 'Ashton', 'Kelley', 'a.kelley@x.com'),
    ('bgray', 'Byron', 'Gray', 'b.gray@x.com'),
    ('medwards', 'Maria', 'Edwards', 'm.edwards@x.com'),
    ('srobinso', 'Savana', 'Robinson', 's.robinson@x.com'),
    ('jperry', 'Jenna', 'Perry', 'j.perry@x.com'),
    ('cphillip', 'Carl', 'Phillips', 'c.phillips@x.com'),
    ('aparker', 'Arnold', 'Parker', 'a.parker@x.com'),
    ('dphillip', 'Dexter', 'Phillips', 'd.phillips@x.com'),
    ('aallen', 'Alford', 'Allen', 'a.allen@x.com'),
    ('dmyers', 'David', 'Myers', 'd.myers@x.com'),
    ('gmason', 'Grace', 'Mason', 'g.mason@x.com'),
    ('jreed', 'Jessica', 'Reed', 'j.reed@x.com'),
    ('aandrews', 'Arnold', 'Andrews', 'a.andrews@x.com'),
    ('smiller', 'Sam', 'Miller', 's.miller@x.com'),
    ('ehill', 'Ellia', 'Hill', 'e.hill@x.com'),
    ('kfoster', 'Kevin', 'Foster', 'k.foster@x.com'),
    ('oturner', 'Olivia', 'Turner', 'o.turner@x.com'),
    ('rperkins', 'Rafael', 'Perkins', 'r.perkins@x.com'),
    ('welliott', 'Walter', 'Elliott', 'w.elliott@x.com'),
    ('mwells', 'Max', 'Wells', 'm.wells@x.com'),
    ('fevans', 'Frederick', 'Evans', 'f.evans@x.com'),
    ('amontgom', 'Adele', 'Montgomery', 'a.montgomery@x.com'),
    ('ktaylor', 'Kirsten', 'Taylor', 'k.taylor@x.com'),
    ('fgrant', 'Fenton', 'Grant', 'f.grant@x.com'),
    ('rdixon', 'Ryan', 'Dixon', 'r.dixon@x.com'),
    ('ssmith', 'Sienna', 'Smith', 's.smith@x.com'),
    ('kmorgan', 'Kelvin', 'Morgan', 'k.morgan@x.com'),
    ('drogers', 'Deanna', 'Rogers', 'd.rogers@x.com'),
    ('ballen', 'Briony', 'Allen', 'b.allen@x.com'),
    ('cmitchel', 'Catherine', 'Mitchell', 'c.mitchell@x.com'),
    ('valexand', 'Victor', 'Alexander', 'v.alexander@x.com'),
    ('pwilliam', 'Patrick', 'Williams', 'p.williams@x.com'),
    ('ewatson', 'Edwin', 'Watson', 'e.watson@x.com'),
    ('kryan', 'Kelsey', 'Ryan', 'k.ryan@x.com'),
    ('jalexand', 'Jenna', 'Alexander', 'j.alexander@x.com'),
    ('fbaker', 'Frederick', 'Baker', 'f.baker@x.com'),
    ('jharper', 'Jacob', 'Harper', 'j.harper@x.com'),
    ('brobinso', 'Bruce', 'Robinson', 'b.robinson@x.com'),
    ('dnelson', 'Dale', 'Nelson', 'd.nelson@x.com'),
    ('vpayne', 'Victor', 'Payne', 'v.payne@x.com'),
    ('wmartin', 'Wilson', 'Martin', 'w.martin@x.com'),
    ('cstewart', 'Caroline', 'Stewart', 'c.stewart@x.com'),
    ('ltucker', 'Lilianna', 'Tucker', 'l.tucker@x.com'),
    ('asulliva', 'Ada', 'Sullivan', 'a.sullivan@x.com'),
    ('smorgan', 'Sofia', 'Morgan', 's.morgan@x.com'),
    ('aedwards', 'Adelaide', 'Edwards', 'a.edwards@x.com'),
    ('kreed', 'Kellan', 'Reed', 'k.reed@x.com'),
    ('ahiggins', 'Arianna', 'Higgins', 'a.higgins@x.com'),
    ('jchapman', 'Justin', 'Chapman', 'j.chapman@x.com'),
    ('vclark', 'Vanessa', 'Clark', 'v.clark@x.com'),
    ('rkelly', 'Richard', 'Kelly', 'r.kelly@x.com'),
    ('fsulliva', 'Fiona', 'Sullivan', 'f.sullivan@x.com'),
    ('dmiller', 'Deanna', 'Miller', 'd.miller@x.com'),
    ('lparker', 'Lucy', 'Parker', 'l.parker@x.com'),
    ('adavis', 'Aiden', 'Davis', 'a.davis@x.com'),
    ('sholmes', 'Sawyer', 'Holmes', 's.holmes@x.com'),
    ('athomas', 'Audrey', 'Thomas', 'a.thomas@x.com'),
    ('swells', 'Stella', 'Wells', 's.wells@x.com'),
    ('fmartin', 'Florrie', 'Martin', 'f.martin@x.com'),
    ('rreed', 'Roland', 'Reed', 'r.reed@x.com'),
    ('cwatson', 'Catherine', 'Watson', 'c.watson@x.com'),
    ('frussell', 'Frederick', 'Russell', 'f.russell@x.com'),
    ('cjones', 'Cadie', 'Jones', 'c.jones@x.com'),
    ('jrichard', 'Jordan', 'Richardson', 'j.richardson@x.com'),
    ('amiller', 'Adam', 'Miller', 'a.miller@x.com'),
    ('mrussell', 'Michelle', 'Russell', 'm.russell@x.com'),
    ('sryan', 'Sarah', 'Ryan', 's.ryan@x.com'),
    ('vhall', 'Vivian', 'Hall', 'v.hall@x.com'),
    ('ephillip', 'Evelyn', 'Phillips', 'e.phillips@x.com'),
    ('hhunt', 'Haris', 'Hunt', 'h.hunt@x.com'),
    ('sfoster', 'Steven', 'Foster', 's.foster@x.com'),
    ('dallen', 'Derek', 'Allen', 'd.allen@x.com'),
    ('crobinso', 'Cherry', 'Robinson', 'c.robinson@x.com'),
    ('eroberts', 'Edwin', 'Roberts', 'e.roberts@x.com'),
    ('amorriso', 'Alisa', 'Morrison', 'a.morrison@x.com'),
    ('smoore', 'Savana', 'Moore', 's.moore@x.com'),
    ('jwarren', 'Julian', 'Warren', 'j.warren@x.com'),
    ('bbarnes', 'Belinda', 'Barnes', 'b.barnes@x.com'),
    ('omason', 'Olivia', 'Mason', 'o.mason@x.com'),
    ('mcole', 'Miranda', 'Cole', 'm.cole@x.com'),
    ('tbailey', 'Tara', 'Bailey', 't.bailey@x.com'),
    ('tcole', 'Ted', 'Cole', 't.cole@x.com'),
    ('khenders', 'Kristian', 'Henderson', 'k.henderson@x.com'),
    ('hsulliva', 'Heather', 'Sullivan', 'h.sullivan@x.com'),
    ('shall', 'Stella', 'Hall', 's.hall@x.com'),
    ('imurray', 'Isabella', 'Murray', 'i.murray@x.com'),
    ('eferguso', 'Eddy', 'Ferguson', 'e.ferguson@x.com'),
    ('lmartin', 'Lyndon', 'Martin', 'l.martin@x.com'),
    ('redwards', 'Ryan', 'Edwards', 'r.edwards@x.com'),
    ('darmstro', 'Dainton', 'Armstrong', 'd.armstrong@x.com'),
    ('dbailey', 'Daryl', 'Bailey', 'd.bailey@x.com'),
    ('jmontgom', 'Jacob', 'Montgomery', 'j.montgomery@x.com'),
    ('rbrown', 'Rafael', 'Brown', 'r.brown@x.com'),
    ('irobinso', 'Isabella', 'Robinson', 'i.robinson@x.com'),
    ('mstevens', 'Max', 'Stevens', 'm.stevens@x.com'),
    ('nfarrell', 'Nicole', 'Farrell', 'n.farrell@x.com'),
    ('mkelly', 'Madaline', 'Kelly', 'm.kelly@x.com'),
    ('kjohnson', 'Kate', 'Johnson', 'k.johnson@x.com'),
    ('devans', 'Darcy', 'Evans', 'd.evans@x.com'),
    ('fbailey', 'Freddie', 'Bailey', 'f.bailey@x.com'),
    ('hstevens', 'Haris', 'Stevens', 'h.stevens@x.com'),
    ('rstevens', 'Ryan', 'Stevens', 'r.stevens@x.com'),
    ('lmason', 'Lucas', 'Mason', 'l.mason@x.com'),
    ('eross', 'Ellia', 'Ross', 'e.ross@x.com'),
    ('fgray', 'Fenton', 'Gray', 'f.gray@x.com'),
    ('mcasey', 'Martin', 'Casey', 'm.casey@x.com'),
    ('rmitchel', 'Rosie', 'Mitchell', 'r.mitchell@x.com'),
    ('cmiller', 'Carlos', 'Miller', 'c.miller@x.com'),
    ('sthompso', 'Sabrina', 'Thompson', 's.thompson@x.com'),
    ('mgrant', 'Myra', 'Grant', 'm.grant@x.com'),
    ('lgrant', 'Lana', 'Grant', 'l.grant@x.com'),
    ('acooper', 'April', 'Cooper', 'a.cooper@x.com'),
    ('charriso', 'Charlotte', 'Harrison', 'c.harrison@x.com'),
    ('sroberts', 'Savana', 'Roberts', 's.roberts@x.com'),
    ('cchapman', 'Chloe', 'Chapman', 'c.chapman@x.com'),
    ('ccampbel', 'Carlos', 'Campbell', 'c.campbell@x.com'),
    ('lrogers', 'Lana', 'Rogers', 'l.rogers@x.com'),
    ('lferguso', 'Lyndon', 'Ferguson', 'l.ferguson@x.com'),
    ('lbaker', 'Lucy', 'Baker', 'l.baker@x.com'),
    ('dellis', 'Dainton', 'Ellis', 'd.ellis@x.com'),
    ('mphillip', 'Myra', 'Phillips', 'm.phillips@x.com'),
    ('cbarrett', 'Carina', 'Barrett', 'c.barrett@x.com'),
    ('csmith', 'Chloe', 'Smith', 'c.smith@x.com'),
    ('pstevens', 'Paul', 'Stevens', 'p.stevens@x.com'),
    ('showard', 'Sydney', 'Howard', 's.howard@x.com'),
    ('swright', 'Sam', 'Wright', 's.wright@x.com'),
    ('rallen', 'Richard', 'Allen', 'r.allen@x.com'),
    ('hcrawfor', 'Henry', 'Crawford', 'h.crawford@x.com'),
    ('sgrant', 'Sienna', 'Grant', 's.grant@x.com'),
    ('jwatson', 'Jared', 'Watson', 'j.watson@x.com'),
    ('dsulliva', 'Dominik', 'Sullivan', 'd.sullivan@x.com'),
    ('dbarrett', 'Dale', 'Barrett', 'd.barrett@x.com'),
    ('harmstro', 'Henry', 'Armstrong', 'h.armstrong@x.com'),
    ('ljohnsto', 'Lenny', 'Johnston', 'l.johnston@x.com'),
    ('gjohnsto', 'Grace', 'Johnston', 'g.johnston@x.com'),
    ('twarren', 'Tony', 'Warren', 't.warren@x.com'),
    ('mharper', 'Miller', 'Harper', 'm.harper@x.com'),
    ('tmoore', 'Tara', 'Moore', 't.moore@x.com'),
    ('aelliott', 'Abigail', 'Elliott', 'a.elliott@x.com'),
    ('awest', 'Aston', 'West', 'a.west@x.com'),
    ('vdixon', 'Valeria', 'Dixon', 'v.dixon@x.com'),
    ('abarnes', 'Arthur', 'Barnes', 'a.barnes@x.com'),
    ('alloyd', 'Alina', 'Lloyd', 'a.lloyd@x.com'),
    ('nharriso', 'Ned', 'Harrison', 'n.harrison@x.com'),
    ('dclark', 'Derek', 'Clark', 'd.clark@x.com'),
    ('vferguso', 'Victoria', 'Ferguson', 'v.ferguson@x.com'),
    ('cgibson', 'Carlos', 'Gibson', 'c.gibson@x.com'),
    ('ffoster', 'Fiona', 'Foster', 'f.foster@x.com'),
    ('dstewart', 'Darcy', 'Stewart', 'd.stewart@x.com'),
    ('probinso', 'Paul', 'Robinson', 'p.robinson@x.com'),
    ('bhunt', 'Belinda', 'Hunt', 'b.hunt@x.com'),
    ('afoster', 'Aiden', 'Foster', 'a.foster@x.com'),
    ('sevans', 'Samantha', 'Evans', 's.evans@x.com'),
    ('rhill', 'Reid', 'Hill', 'r.hill@x.com'),
    ('mowens', 'Maddie', 'Owens', 'm.owens@x.com'),
    ('sellis', 'Sophia', 'Ellis', 's.ellis@x.com'),
    ('kcole', 'Kristian', 'Cole', 'k.cole@x.com'),
    ('mclark', 'Michael', 'Clark', 'm.clark@x.com'),
    ('rpayne', 'Rebecca', 'Payne', 'r.payne@x.com'),
    ('bmitchel', 'Brad', 'Mitchell', 'b.mitchell@x.com'),
    ('djohnsto', 'Daryl', 'Johnston', 'd.johnston@x.com'),
    ('malexand', 'Max', 'Alexander', 'm.alexander@x.com'),
    ('tsulliva', 'Tara', 'Sullivan', 't.sullivan@x.com'),
    ('bedwards', 'Blake', 'Edwards', 'b.edwards@x.com'),
    ('rparker', 'Ryan', 'Parker', 'r.parker@x.com'),
    ('amitchel', 'Amber', 'Mitchell', 'a.mitchell@x.com'),
    ('tmorgan', 'Ted', 'Morgan', 't.morgan@x.com'),
    ('nowens', 'Ned', 'Owens', 'n.owens@x.com'),
    ('cpayne', 'Charlie', 'Payne', 'c.payne@x.com'),
    ('dtaylor', 'Daisy', 'Taylor', 'd.taylor@x.com'),
    ('dhill', 'Derek', 'Hill', 'd.hill@x.com'),
    ('hfoster', 'Honey', 'Foster', 'h.foster@x.com'),
    ('cwilliam', 'Caroline', 'Williams', 'c.williams@x.com'),
    ('mwest', 'Michael', 'West', 'm.west@x.com'),
    ('wallen', 'Wilson', 'Allen', 'w.allen@x.com'),
    ('abarrett', 'Adrianna', 'Barrett', 'a.barrett@x.com'),
    ('dharriso', 'Derek', 'Harrison', 'd.harrison@x.com'),
    ('dpayne', 'Dominik', 'Payne', 'd.payne@x.com'),
    ('dwalker', 'Dale', 'Walker', 'd.walker@x.com'),
    ('amurray', 'Alan', 'Murray', 'a.murray@x.com'),
    ('lhunt', 'Lana', 'Hunt', 'l.hunt@x.com'),
    ('jcampbel', 'Jacob', 'Campbell', 'j.campbell@x.com'),
    ('ebailey', 'Ellia', 'Bailey', 'e.bailey@x.com'),
    ('cevans', 'Cadie', 'Evans', 'c.evans@x.com'),
    ('fmoore', 'Freddie', 'Moore', 'f.moore@x.com'),
    ('bmontgom', 'Briony', 'Montgomery', 'b.montgomery@x.com'),
    ('ahamilto', 'Amelia', 'Hamilton', 'a.hamilton@x.com'),
    ('ehall', 'Emma', 'Hall', 'e.hall@x.com'),
    ('cryan', 'Carina', 'Ryan', 'c.ryan@x.com'),
    ('vmyers', 'Vivian', 'Myers', 'v.myers@x.com'),
    ('jriley', 'James', 'Riley', 'j.riley@x.com'),
    ('aross', 'Adrian', 'Ross', 'a.ross@x.com'),
    ('aferguso', 'Amelia', 'Ferguson', 'a.ferguson@x.com'),
    ('fmitchel', 'Frederick', 'Mitchell', 'f.mitchell@x.com'),
    ('jrussell', 'Joyce', 'Russell', 'j.russell@x.com'),
)


def randobj(objs):
    return objs.objects.all()[randint(0, objs.objects.count() - 1)]


line = 1
for (u, f, l, e) in specs[:to_generate]:
    usr = User(username=u, first_name=f, last_name=l, email=e)
    if set_pass:
        usr.set_password(u + '1')

    try:
        usr.save()
    except Exception:
        print(f'Unable to create Student(User) {line} {u} ({f} {l})')
    else:
        m = randobj(Major)
        s = Student(user=usr, major=m)
        s.save()

        start = randint(0, Semester.objects.count() - 1)
        stop = start + randint(1, 12)
        for sem in Semester.objects.all().order_by("date_started")[start:stop]:
            sems = SemesterStudent(student=s, semester=sem)
            sems.save()

        print(f'create stud {line} {u} ({f} {l}) {m}')
    line = line + 1
