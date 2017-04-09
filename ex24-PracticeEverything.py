print "Let's practice everything."
#escapes '\' are needed to use hyphenation that might otherwise be confused as an end-of-string character
print 'You\'d need to know \'bout excapes with \\ that do \n newlines and \t tabs.'

#this is a lonnnnng string using 'escapes' for newlines and tabs
poem = """
\tThe lovely world
with logic so fimrly planted
canot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none:
"""

print "__________________"
print poem
print "__________________"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

#this is a 'function' that is passed in a variable used locally as 'started'
#the function 'returns' three variables
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
print "with a starting point of: %d" % start_point
#the function 'returns' three variables
beans, jars, crates = secret_formula(start_point)
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

