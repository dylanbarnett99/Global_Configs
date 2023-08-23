# Import the DHCPServer module
Import-Module DHCPServer

#
#### Change for each scope ####
#

# Replace with the DHCP server
$DHCPServer = "10.6.60.51" 

#Set Scope ID
#### edit #### 
#the Scope ID value will default correctly when creating the scope
$scopeID = "10.253.1.0"

# Set the scope name
$scopeName = "xxxx Test ES MC Admin"

# Set the start and end IP addresses
$startIP = "10.253.1.20"
$endIP = "10.253.1.254"

# Set the subnet mask
$subnetMask = "255.255.255.0"

# Set the default gateway
$gateway = "10.253.200.1"

#Set the Primary Server relationship variable
$PrimaryServer = "entdhcp001.cmsdomain.cms.k12.nc.us-entdhcp002.cmsdomain.cms.k12.nc.us"

#Set the Secondary Server variable
$SecondaryServer = "entdhcp002.cmsdomain.cms.k12.nc.us"

#
#### SHOULD NOT CHANGE ####
#

# Set the DNS Server
$dnsServer = "10.6.67.30, 10.6.67.33, 10.6.66.20, 10.6.66.21"

# Set the DNS domain
$dnsDomain = "cmssites.cms.k12.nc.us.com"

# Set the lease length
$leaseLength = "4.00:00:00"

##################
# Create the scope
Add-DhcpServerv4Scope -ComputerName $DHCPServer -Name $scopeName -Description $scopeName -StartRange $startIP -EndRange $endIP -SubnetMask $subnetMask -DNSDomain $parentDomain -LeaseDuration $leaseLength

# Add default gate into the scope
Set-DhcpServerv4Scope -ComputerName $DHCPServer -ScopeName $scopeName -Router $gateway 

#Cofigure the DNS Settings for the scope
#
#Get-DhcpServerv4Scope -ComputerName $DHCPServer -ScopeID $scopeID | Set-DhcpServerv4OptionValue -ComputerName $DHCPServer -DnsServer $dnsServer
#
Set-DhcpServerv4OptionValue -ComputerName $DHCPServer -ScopeID $scopeID -DnsServer $dnsServer

# Check if the DNS server went int correctly
Get-DhcpServerv4Scope -ComputerName $DHCPServer -ScopeID $scopeID | Get-DhcpServerv4OptionValue -ComputerName $DHCPServer | Where-Object {$_.OptionID -like 6} | FT Value

# Configure the failover
Set-DhcpServerv4Failover -ComputerName $DHCPServer -ScopeName $scopeName -PrimaryServer $PrimaryServer -SecondaryServer $SecondaryServer

# Enable the scope
#Enable-DhcpServerv4Scope -ScopeName $scopeName