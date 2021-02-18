from html.parser import HTMLParser

### Parser ###
# Class and function definitions
class HCDP_HTML_Parser(HTMLParser):
    tag_list  = [] # filled by handle_starttag()
    link_list = [] # filled by parse_for_links()

    def parse_for_links(self, pattern):
        for tag in self.tag_list:                             # for every tag in the file,
            if tag[0] == 'a':                                 # check if it's an <a> tag.
                for attr in tag[1]:                           # for each attribute of the <a> tag,
                    if attr[0] == 'href':                     # check if there's an href in it.
                        if pattern in attr[1]:                # if the data field of the href matches,
                            self.link_list.append(attr[1])    # append it to the list of rel-links.

    def handle_starttag(self, tag, attrs):
        self.tag_list.append([tag, attrs])