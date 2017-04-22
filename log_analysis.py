# http://qiita.com/chocolatampcoffee/items/9887c5ee3a528ba43720
# https://github.com/INC-i/CCstuff

import sys
import ccstuff

LOG_FILE = "/var/log/apache2/access.log.1"
ccobj = ccstuff.rir()

def main():
	ip_addresses = []

	# extract IP addresses to list(ip_addresses)
	for line in open(LOG_FILE):
		ip_address = line.split()[0]
		ip_addresses.append(ip_address)

	# extract country num to dict(country_num)
	country_num	= accumulate_country(ip_addresses)
	print "\n<(1) each country's number of IPaddress from ip_list>"
	for key, num in sorted(country_num.items(), key=lambda x:x[1], reverse=True):
		country_name	= ccobj.cctoname(key)[0]
		print "%6d: %s" %(num, country_name)
	
	# extract country num from uniq IP addresses to dict(uniq_num)
	ip_uniq 	= list(set(ip_addresses))
	uniq_num	= accumulate_country(ip_uniq)
	print "\n<(2) each country's number of IPaddress from ***uniq*** ip_list>"
	for key, num in sorted(uniq_num.items(), key=lambda x:x[1], reverse=True):
		country_name	= ccobj.cctoname(key)[0]
		print "%6d: %s" %(num, country_name)

	# calculate ALL/UNIQ nummber
	all_uniq_num	= all_divided_by_uniq(country_num, uniq_num)
	print "\n<(3) ALL(1)/UNIQ(2)>"
	for key, num in sorted(all_uniq_num.items(), key=lambda x:x[1], reverse=True):
		country_name	= ccobj.cctoname(key)[0]
		print "%6d: %s" %(num, country_name)


# calculate (all / uniq)
def all_divided_by_uniq(_all, uniq):
	all_uniq	= {}
	for key, num in uniq.items():
		all_uniq[key]	= float(_all[key]) / uniq[key]
	return all_uniq
	

# accumulate ip num per country
def accumulate_country(ip_list):
	country_dict	= {}
	for ip in ip_list:
		country	= ccobj.ipv4tocc(ip)
		if country	== None:
			continue
		if country_dict.has_key(country):
			country_dict[country] = country_dict[country] +1 
		else:
			country_dict[country] = 1
	return country_dict
	
if __name__ =="__main__":
	main()
	
