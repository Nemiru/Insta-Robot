# imports
from instapy import InstaPy
from instapy import smart_run

insta_username = 'yas'
insta_password = 'nas'


session = InstaPy(username = insta_username,
	              password = insta_password,
	              headless_browser=True),
#'session.login(),

with smart_run(session):

  hastags=['studying','accountant','accounting'
   ,'finance','business','accountancyblog','cimalife'
   "mycimalife", "cimastudent", "accountingstudent",
   "cimaexams","career","careergoals","cimacareer","managementaccounting"
   "acca","students","school","college","future","education",
   "studynotes", "business", "charteredaccountant","accagoals", 
   "studysuccess","finance","studysmart","accaexams","tax","inspiration",
   "givevalue","personalgrowth","leader bookkeeping","follow4followback",
   "follow4like","followandlike","like","follower","followme" ,"#following",
   "followforfollowback","followmeplease","follow","followｍe","likeforlikes",
   "like4likes","likeforfollow","likelike","liker","likeforlikeback",
   "5likesfor5likes","6likesfor6likes','likesforlike"],
  
#how it will interact with accounts
session.set_relationship_bounds(enabled=True,
  	                              delimit_by_numbers=True,
  	                              max_followers=600,
  	                              min_followers=35,
  	                              min_following=60,
                                  min_posts=2,
  	                              ),

#delay per each action: eg like by tags wait 15secs then repeat
session.set_action_delays(enabled=True,
                         like_by_tags=15,
                follow_user_followers=4.17,
                           set_dont_like=6),

# how to go about liking hastags		
session.like_by_tags(hastags,amount=40,skip_top_posts=True,
  	  interact=True),                  

# how interact with users, from liked tags, and follow users
session.set_user_interact(amount=3, randomize=True,percentage=100),

#skip users with private accounts,no profile pics and 60% of business accounts
session.set_skip_users(skip_private=True,
                       skip_no_profile_pic=True,no_profile_pic_percentage=100,
                       skip_business=True, business_percentage=60
                      ),

# interact with posts of this language character 
session.set_mandatory_language(enabled=True, character=['LATIN']),


# follow these users followers (10 each) and randomize selection
session.follow_user_followers([
'awlindia','axbotic','cpa4it','russellminds','ultimateabundance','ichoosebirmingham','marta_studies_acca_',
'accablog','noelleattard','studiesaccounting','accountingaccastudentlife','account_ability1',
'acca.study','james_wright_acca','mycimalife','cimaglobal','acca.motivation','acca_uk', 'acca.official',
'themuslimahaccountant','help.assignments','independentbirmingham','ucas_online','birmingham.city',
'the_library_of_birmingham','birminghamhistory','bhamstories','birmingham_archives','notyouraveragestudent',
'livingwellbrum','redbrickmarketbirmingham','therollingmilljq','onlybirmingham','promotebusinessuk',
'bcu_mindfulness','uobs_sixthform','uobschool','unibirmingham','astonuniversity','mybcu',
'accesscreativecollege','oxford_unibhamupdates','iccbirmingham','nhswebsite','post16education',
'apprentice.uk','crescentcollegebirmingham'], amount=10, randomize=True, interact=True),

#things to not like/avoid
session.set_dont_like(["sex","sexy","foodie","foodporn","fun","instafood",
  "travelling","tasty","tourism","yummy","cute","tbt","selfie","summer",
  "friends","nature","girl","fitness","life","instamood","memes","dirtymemes",
  "murder","sucide","hurtingpeople","bullying","rudememes","makeup","fashion",
  "clothes","cars","foods","funnyvideos","swearwords","hair","skincare","products",
  "games","tiktok","music","technology","piercings","tattoos","sport","decor",
  "art","beauty","TV&Movies","comics","Shops","shopping","DIY","places"]),


# sessions ends, threaded session?
session.end(threaded_session=True)