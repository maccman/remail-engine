Remail is RESTful email for Rails.

Forget configuring SMTP servers and queues, just use Remail. 
Remail uses Google App Engine to send and receive emails RESTfully.

# Features
* POST emails to your Remail App Engine in order to send them
* Remail POSTS received emails back to a configurable URL

# Setup
* Configure settings.yaml:
  * Create a random api_key, for example using uuidgen.
  * Add a publicly accessible callback url.
* Upload the engine to Google App Engine (see their [docs](http://code.google.com/appengine/docs/))
* Install the [Remail gem](http://github.com/maccman/remail) (sudo gem install remail).

# Feature ideas
* Retry POST callbacks if they fail.
* Attachment support.