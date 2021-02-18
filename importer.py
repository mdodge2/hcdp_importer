from hcdp_parser import HCDP_HTML_Parser
import gateway_functions

# Set things up
webpage = open('site/downloads.html', 'r', encoding='utf-8')
webpage_str = webpage.read()
link_parser = HCDP_HTML_Parser()

# Run the file through the parser
link_parser.feed(webpage_str)
link_parser.parse_for_links('/files/')
links = link_parser.link_list
print(links)

# Upload the list to the gateway
for link in links: #TODO convert relative links to absolute
    gateway_functions.import_data_to_ikewai_by_link(link=link)