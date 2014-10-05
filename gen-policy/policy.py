import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.render("input_config.html")

    def post(self):
	num_of_policy = self.request.get("num_of_policy")
	zone_A = self.request.get("zone_A")
	zone_B = self.request.get("zone_B")
	Interface_A = self.request.get("Interface_A")
	Interface_B = self.request.get("Interface_B")
    	logging = self.request.get("logging")
    	count = self.request.get("count")
	params = dict(num_of_policy = num_of_policy,
			zone_A = zone_A,
			zone_B = zone_B,
			Interface_A = Interface_A,
			Interface_B = Interface_B,
    			logging = logging,
    			count = count)
	if not (num_of_policy and zone_A and zone_B):
        	self.render("input_config.html",**params)
	else:
        	self.render("output_config.html",**params)

app = webapp2.WSGIApplication([('/',MainPage),
                              ],
                              debug=True)
