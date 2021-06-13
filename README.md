NOTE: this software uses Selenium WebDriver library for python, if you interested in using this software please install selenium webdriver with pip installer

	-pip install selenium

once you have installed the library, you need to call the library selenium and the function facebot:

	from facebot import facebot


	facebot.put(
			type,
		   	attr,
			info,
			offset,
			driver,
	)
			
type: refers as type of html tag, like "input" or "button"

attr: you putting a html attribute and the value of this, like "placeholder" or "type", "href" or whatever you consider important to locate the html element

info: the information you need to put in whatever form, like input text

offset: the delay of an action in seconds

driver: the driver you are using


this "library" is so easy to use, if you need "help" to know how to use it, please do not hesitate to enter in the examples folder 
 
a simple example would be like this:

	facebot.put("input", "name='email'", "your@email.com" , 20, driver)
	facebot.put("button", "value='send'", offset=20, driver=driver)
