 create a web portfolio and a resume using Python and Json so this is the process that I personally use to update my own portfolio and resume and I think a lot of you are going to find this useful so if you only have a resume and don't have a web portfolio with a URL that you can send to a potential employer then I think you're really limiting yourself in terms of uh who you might be able to get your information in
Show less
00:27
front of for potential jobs uh but having mult versions of something like this uh can be a bit of a pain when you want to make updates uh so in this video I'm going to show how I use Python and Json to create both versions of these from a single source of data so that they're never out of sync and you don't have to go in and update each of those manually uh you just have to update your Json file and both of them get generated simultaneously uh to show you what I mean let's look at the finished product
Read More
00:56
of what we'll be creating in this video so a while back in my community tab I asked you all to send me in some examples of your current resumés and I took a lot of inspiration from those in order to create a template of both a web portfolio and a resume that I think is going to work for a lot of you and I'm just using a custom CSS stylesheet that I created to style this so if you don't necessarily like the style and you know some CSS uh then this should be super easy for you to update to and add your
Read More
01:26
own customizations um and even style it completely from scratch if you'd like uh with CSS uh you basically have unlimited styling options so here we have the web portfolio and this would be something that you'd host on a website that you can send to employers these are usually a bit more relaxed than a traditional resume and allow you to show a bit more of your personality so here you can see that I have a couple of social media links in here uh there are some images further down I list some hobbies and
Read More
01:57
interests and things like that and I also styled this to be responsive uh so if we resize this um then it should uh respond accordingly and look good on uh smaller Windows as well so on mobile or um desktop now with this same data I also generated a more traditional looking resumé uh that's using a strip down version of that same data uh so this is this here and we can see that uh this resume is more traditional and More in line with uh what companies expect to see when you send them a resume in PDF
Read More
02:36
or print form so I've taken out the social media links I've removed the images and we don't have things like interest or Hobbies or anything like that um I think it's fine to put interests or hobbies in some uh traditional resumés if you have the room uh but for this example I just wanted this to fit onto a single page uh when we printed this so if I go to print this then we can see that this fits nicely on one page and we can also easily uh save this as a PDF so that's the portfolio
Read More
03:07
and resume that are both generated within python both of them are static HTML files which means that they uh don't need any backend code to serve them up and are also a lot easier to deploy uh so let's take a look at the data that was used to generate these pages and then we'll go over the python code that ties all of this together so let me bring up my vs code here so I have a lot of these files already created here and all of the code from this video is going to be available on my GitHub and I'll leave a link to that
Read More
