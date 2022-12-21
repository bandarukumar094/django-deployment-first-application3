from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request): #view-function
    print("wecome/ url is requested & display()is executed");
    print(type(request))
    #ss----> is html-data/code
    ss = '''
            <center>
                <h2 style="color:Blue;">
                    Hello user, welcome to Django First-project
                    First-App
                </h2>
                <hr/>
            </center>
        ''';
    return HttpResponse();
    
    
def show(request):
    print("hello user");
    ss='''
            <!--
        HTML Webpage to display 'welcome-Message' with different Headings
        (F:\pavan\html\welcome.html)
-->

<html>
    <head>
        <title>***welcome-page***</title>
        <style>
                h1{
                    color:Blue;
                }
                h2{
                    color:Green;
                }
                h3{
                    color:Red;
                }
                h4{
                    color:Orange
                }
                h5{
                    color:Pink;
                }
                h6{
                    color:Violet;
                }
                h1,h3,h5{
                        background-color:yellow;
                }
                h2,h4,h6{
                        background-color:lightblue;
                }
        </style>
    </head>
    <body>
        <center>
                <h1>welcome to DJANGO HTML webpage</h1>
                <hr color='brown' width='95%'/>
                <h2>welcome to DJANGO HTML webpage</h2>
                <hr color='brown' width='85%'/>
                <h3>welcome to DJANGO HTML webpage</h3>
                <hr color='brown' width='75%'/>
                <h4>welcome to DJANGO HTML webpage</h4>
                <hr color='brown' width='65%'/>
                <h5>welcome to DJANGO HTML webpage</h5>
                <hr color='brown' width='55%'/>
                <h6>welcome to DJANGO HTML webpage</h6>
                <hr color='brown' witdh='45%'/>          
         </center>
     </body>
 </html>
    ''';
    return HttpResponse(ss);
    
    
    
def hello(request):
    #print("hello/ url is requested & hello() is executed");
    ss='''
    <html>
        <head>
            <title>Hello webpage</title>
            <style>
                h1{
                    color:Blue;                  
                }
                h2{
                    color:Green;
                }
                h3{
                    color:Red;
                }
                h1,h2,h3{
                    background-color:plum;
                    witdh:60%;
                    border:2px Solid Brown;
                }
            </style>
        </head>
        <body>
            <center>
                <h1>Hello User..!!!</h1>
                <hr color='brown' width='80%'/>
                <h2>welcome to Django-App</h2>
                <hr color='brown' width='60%'/>
                <h3>Have a nice day...</h3>
                <hr color='brown' width='40%'/>
            </center>
        </body>
    </html>
    ''';
    return HttpResponse(ss);
    
    
import time;	
def senddatetime(request):
	print("dtime/ url is requested & senddatetime() is executed");
	ct = time.ctime()
	print("Client Request Date & time on server :: ",ct);
	ss='''
	<html>
		<head>
			<title>Date-time Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightgreen;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Welcome to DJango-User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Server-Date & Time :: </h2>
				<hr color='brown' width='70%'/>
				<h3>''',ct,'''</h3>
				<hr color='brown' width='60%'/>
			</center>
		</body>
	</html>
	''';
	return HttpResponse(ss);
    
def demo(request):   
	print("mulitple-Requests-URLs same respose");
	htmldata='''<center>
		<h1>Welcome Demo User!!!</h1>
		<hr />
		<h2>This is Same-Output for diff-mulitple-Requests-URLs</h2>
		<hr />
		<h3>Have a Great Day...</h3>
		</center>''';
	return HttpResponse(htmldata);
    
#default-url-request-view-func
def homepage(request):
    htmldata='''<center>
        <h1>Welcome to DEFAULT Home-Page!!!</h1>
        <hr />
        <h2>Your Request Page is Not-Found...</h2>
        <hr />
        <h3>Plz try other URL or Links!!!</h3>
    </center>''';
    return HttpResponse(htmldata);


    
    

    
            
    
        
        
              

