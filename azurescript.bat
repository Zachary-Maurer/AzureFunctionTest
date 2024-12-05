CALL az group create --name AzureFunctionsQuickstart-rg --location eastus
CALL az storage account create --name zmstorage1 --location eastus --resource-group AzureFunctionsQuickstart-rg --sku Standard_LRS
CALL az functionapp create --resource-group AzureFunctionsQuickstart-rg --consumption-plan-location eastus --runtime python --runtime-version 3.11 --functions-version 4 --name azuretestzm --os-type linux --storage-account  zmstorage1
CALL func azure functionapp publish azuretestzm
CALL az functionapp keys set --resource-group AzureFunctionsQuickstart-rg --name azuretestzm --key-type functionKeys --key-name default
