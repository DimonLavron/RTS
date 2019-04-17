from flask import Flask, render_template,request, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("db:27017") #host uri
db = client.mymongodb #database
events_col = db.events #collection name

@app.route("/")
def main_page():
	title = "Main Page"
 	return render_template("main.html", t=title)

@app.route("/post", methods=['POST'])
def post():
	class Event:
		def __init__(self, checkpoint_id, tag, time):
	 		self.checkpoint_id = checkpoint_id
	 		self.tag = tag
	 		self.time = time

	event1 = Event("10", "e280116060000206699a8abe4879", "2019-04-06 17:33:12")
	event2 = Event("20", "e280116060000206699a8abe4879", "2019-04-06 17:55:23")
	event3 = Event("30", "e280116060000206699a8abe4879", "2019-04-06 18:11:45")
	event4 = Event("40", "e280116060000206699a8abe4879", "2019-04-06 18:55:14")
	events_col.insert_many([
	{"checkpoint_id":event1.checkpoint_id, "tag":event1.tag, "time":event1.time},
	{"checkpoint_id":event2.checkpoint_id, "tag":event2.tag, "time":event2.time},
	{"checkpoint_id":event3.checkpoint_id, "tag":event3.tag, "time":event3.time},
	{"checkpoint_id":event4.checkpoint_id, "tag":event4.tag, "time":event4.time}
	])
	return redirect("/table")

@app.route("/table")
def read():
	title = "Table"
	heading = "Table with events"

	list = []
	for events in events_col.find() :
	   list.append(events)
	list.reverse()
	return render_template("table.html",events = list, t=title, h=heading)

if __name__ == "__main__":

	app.run(debug=True)
# host="0.0.0.0"
