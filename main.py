from cloud_operator import CloudOperator
import time

from local_storage_manager import GoogleTakeoutManager


# Open Google Drive supporting docs and highlight why this part of the project is not executable.

web_address = "https://support.google.com/accounts/answer/7675428?hl=en"

c_operator = CloudOperator()
c_operator.open_web_browser(web_address)
c_operator.highlight_important_statement()

time.sleep(5)

c_operator.close()

file_operator = GoogleTakeoutManager()
file_operator.run_management_program()
