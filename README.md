# AzureFunctionTest

requirements: 

-Azure Core tools
-Azure CLI
-visual studio code with azure extensions and python extensions
-azurite if you want to emulate with local storage

### Run local instance
If you have everything set up correctly you should see an icon that is shaped like an A.
click on it and enter the information for whatever account you are using.
to start azurite press f1 on the keyboard, search for and select "Azurite: Start"
to run a local instance of the project type "func start"

### Run from Azure
you may be able to skip some of the following steps.
run the following commands from the command line in the same directory as the project
If it asks for your account provide it the neccesary information
IMPORTANT: examine the description of each command to know if you have to modify the command or run it at all

1) az group create --name <RESOURCE GROUP NAME> --location <LOCATION>
run this to create a create a Resource group where <RESOURCE GROUP NAME> is the name of the resource group being created and
<LOCATION> is the closest resource example "eastus". IMPORTANT: If you are part of an organization you
likely will be able to skip this step because they will already have a prexisting resource group set up
you can run this from.

2) az storage account create --name <STORAGE ACCOUNT NAME> --location <LOCATION> --resource-group <RESOURCE GROUP NAME> --sku Standard_LRS
this command creates thee storage for the function and defines its price model.
IMPORTANT: if you are part of an organization they probably have an existing storage account you can use so you can skip this step

3) az functionapp create --resource-group <STORAGE ACCOUNT NAME>g --consumption-plan-location <LOCATION> --runtime python --runtime-version 3.11 --functions-version 4 --name <FUNCTION NAME> --os-type linux --storage-account  <STORAGE ACCOUNT NAME>
this places the function in the storage

4) func azure functionapp publish <FUNCTION NAME>
This publishes the function so it should be available to to call
IMPORTANT: you must attach a key to any calls made to the service by appending ?code=<ACCESS KEY> to the end of any requests made
there are commands you can use to find these or you can find them via the azure website

5) az functionapp keys set --resource-group <RESOURCE GROUP NAME> --name <FUNCTION NAME> --key-type functionKeys --key-name <KEY NAME>
This will make a new key specifically for the function you have just published

IMPORTANT: this will delete the resource group and everything in it
END) az group delete --name <RESOURCE GROUP NAME>
IMPORTANT: this will delete the resource group and everything in it

EXTRA) az functionapp keys list --resource-group <RESOURCE GROUP NAME> --name <FUNCTION NAME>
This will list out the key for the function app.