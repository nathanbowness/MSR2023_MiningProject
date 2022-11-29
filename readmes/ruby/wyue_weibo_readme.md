= Note:

The weibo version 1 api will soon be deprecated and {simsicon}[https://github.com/simsicon] implemented {weibo_2}[https://github.com/simsicon/weibo_2] with oauth2.

= weibo

One of the goals of this gem was to have the same syntax as the twitter gem wherever possible so that it would be easy to learn and use.  Download the gem and give it a try.  Also, I've put together a small demo using sinatra showing how you can use the weibo gem.


To install the gem simply enter:

  gem install weibo
  
To see an example of how it works enter the following into your terminal:

  git clone git://github.com/ballantyne/weibo-example.git
  cd weibo-example
  ruby example.rb

Most of the 新浪微博 api is implemented by this gem.  If I missed something, or Sina added something, please feel free to fork it and add it yourself.  I will do my best to keep the gem up to date.

This gem was made in the process of creating {叽叽喳喳.de}[http://jjzz.de], please take a moment and go and check out that project.  I think that it is a very useful tool for interacting with 新浪微博.

== Sites using the Weibo gem
* {叽叽喳喳.de}[http://jjzz.de]
* {http://weibopi.com/}[http://weibopi.com/]

(Please let me know if your site is using the gem so I can list you here)

== Contributors
* {Feixiong Li}[http://github.com/feixionglee]
* {Aaron Qian}[http://github.com/aq1018]
* {panfu}[https://github.com/panfu]
* {loushizan}[https://github.com/loushizan]
* {numbcoder}[https://github.com/numbcoder]
* {xiuxiu}[https://github.com/xiuxiu]
* {jerrydeng}[https://github.com/jerrydeng]
* {dongyuwei}[https://github.com/dongyuwei]
* {steply}[https://github.com/steply]
* {lgn21st}[https://github.com/lgn21st]
* {reeze}[https://github.com/reeze]
* {many others}[https://github.com/ballantyne/weibo/network/members]


== Note on Patches/Pull Requests
 
* Fork the project.
* Make your feature addition or bug fix.
* Add tests for it. This is important so I don't break it in a
  future version unintentionally.
* Commit, do not mess with rakefile, version, or history.
  (if you want to have your own version, that is fine but bump version in a commit by itself so I can ignore when I pull)
* Send me a pull request. Bonus points for topic branches.

== Special Thanks
This library was based upon and is an adaptation of John Nunemaker's twitter gem.  It started as the twitter gem and has been adapted in the necessary ways to make it work with t.sina.com.cn's api.  I'm using it with his blessing, thanks John.

== Copyright

Copyright (c) 2010 Scott Ballantyne. See LICENSE for details.
