# First Question:
# Refactor the following code using design patterns to make it easier to maintain.
# Second Question:
# Assume this code is proprietary and that you cannot change it with voiding the licence.
# Change this code to add the ability to deal with a new resource type Certificates
# You will have three different kinds of certificates namely:
#  - CherryBlossom_Cert
#  - AWS_Cert
#  - Gov_Cert


import path
import json


class ParseResourceFile:

	def __init__(self, resource_file):
		if path.exists?(resource_file) and path.file?(resource_file):
			resources = json.Parse(resource_files)
			self.CallClients(resources)
		else:
			raise "This is not a file."


	def CallClients(self, resources):
		resource_client = None
		for resource_type in resources:
			for resource in resource_type:
				if "VIP" in resource["type"]:
					resource_client = create_resource_vip(resource)
				elif "Host" in resource["type"]:
					resource_client = create_resource_host(resource)
				elif "Cloudformation" in resource_type["type"]:
					resource_client = create_resource_cloudformation(resource)
				else:
					raise "This is not a valid type."
				resource_client.CreateResource()

	def create_resource_vip(resource):
		vip = None
		if resource["type"] == "NLB_VIP":
			vip = NLB_VIP(resource["vpc"], resource["name"], resource["dns"], resource["owner"], resource["secondary_owner"], 
				resource["department_id"])
			for target in resource["targets"]:
				vip.addTarget(target)
		elif resource["tyoe"] == "ALB_VIP":
			vip = ALB_VIP(resource["vpc"], resource["name"], resource["dns"], resource["owner"], resource["secondary_owner"], 
				resource["department_id"], resource["targets"], resource["istcp?"])
			encryption = SSLEncryption(resource["sslv3?"], resource["public_key"], resource["private_key"])
			vip.setEncryption(encryption)
		elif resource["type"] == "Classic_VIP":
			vip = Classic_VIP(resource["name"], resource["dns"], resource["owner"], resource["secondary_owner"], 
				resource["department_id"], resource["targets"])
		elif resource["type"] == "Legacy_VIP":
			vip = Legacy_VIP(resource["name"], resource["dns"], resource["owner"], resource["secondary_owner"],
			 resource["targets"])
			vip.setBillingId(resource["department_id"])
			owner = Owner(resource["owener"], resource["secondary_owner"])
			vip.setOwner(owner)
		else:
			raise "This is not a valid VIP type."

	def create_resource_host(resource):
		host = None
		if resource["type"] == "EC2_Host":
			host = EC2_HOST(resource["vpc"], resource["dns"], resource["operator"], resource["setup_script"], 
				resource["billing_center"], resource["owner"])
		elif resource["type"] == "StormBreaker_Host":
			host = StormBreaker_Host(resource["vpc"], resource["dns"], resource["operator"], resource["setup_script"], 
				resource["billing_center"], resource["owner"], resource["host_collection"])
		elif resource["type"] == "Retail_Host":
			host = Retail_Host(resource["vpc"], resource["dns"], resource["operator"], resource["setup_script"], 
				resource["billing_center"], resource["owner"], resource["host_collection"])
			host.setRetailId(resource["retail_id"])
		elif resource["type"] == "Legacy_Host":
			host = Legacy_host(resource["vpc"], resource["dns"], resource["operator"], resource["setup_script"], 
				resource["billing_center"], resource["owner"], resource["host_collection"])
			host.setSSHKey(resource["ssh_key"])
		else:
			raise "This is not a valid Host type."


class EC2_HOST:

	def __init__(self, vip, dns, operator, setup_script, billing, owner):
		self.vpc = vip
		self.dns = dns
		self.operator = operator
		self.setup_script = setup_script
		self.department_id = billing
		self.owner = Owner(owner)

	def CreateResource():
		HostClient(self)

class StormBreaker_Host:

	def __init__(self, vip, dns, operator, setup_script, billing, owner):
		self.vpc = vip
		self.dns = dns
		self.operator = operator
		self.setup_script = setup_script
		self.department_id = billing
		self.owner = Owner(owner)

	def CreateResource():
		HostClient(self)

class Retail_Host:

	def __init__(self, vip, dns, operator, setup_script, billing, owner, host_collection):
		self.vpc = vip
		self.dns = dns
		self.operator = operator
		self.setup_script = setup_script
		self.department_id = billing
		self.owner = Owner(owner)
		self.host_collection = host_collection

	def setRetailId(retail_id):
		self.retail_id = retail_id

	def CreateResource():
		HostClient(self)


class Legacy_host:

	def __init__(self, vip, dns, operator, setup_script, billing, owner, host_collection):
		self.vpc = vip
		self.dns = dns
		self.operator = operator
		self.setup_script = setup_script
		self.department_id = billing
		self.owner = Owner(owner)
		self.host_collection = host_collection

	def setSSHKey(ssh_key):
		self.ssh_key = ssh_key

	def CreateResource():
		HostClient(self)




class NLB_VIP:

	def __init__(self, vpc, name, dns, owner, secondary_owner, department_id):
		self.owner = Owner(owner, secondary_owner)
		self.vpc = vpc
		self.name = name
		self.dns = dns
		self.department_id = department_id
		self.targets = None

	def addTarget(target):
		self.targets.append(target)


	def CreateResource():
		VIPClient(self)

class ALB_VIP:

	def __init__(self, vpc, name, dns, owner, secondary_owner, department_id, targets):
		self.owner = Owner(owner, secondary_owner)
		self.vpc = vpc
		self.name = name
		self.dns = dns
		self.department_id = department_id
		self.targets = targets

	def setEncryption(encryption):
		self.encryption = encryption


	def CreateResource():
		VIPClient(self)


class Classic_VIP:

	def __init__(self, name, dns, owner, secondary_owner, department_id, targets):
		self.owner = Owner(owner, secondary_owner)
		self.name = name
		self.dns = dns
		self.department_id = department_id
		self.targets = targets


	def CreateResource():
		VIPClient(self)


class Legacy_VIP:

	def __init__(self, name, dns, owner, secondary_owner, department_id, targets):
		self.owner = Owner(owner, secondary_owner)
		self.name = name
		self.dns = dns
		self.department_id = department_id
		self.targets = targets

	def setBillingId(self, billing):
		self.department_id = billing

	def setOwner(self, owner):
		self.owner = owner


	def CreateResource():
		VIPClient(self)




