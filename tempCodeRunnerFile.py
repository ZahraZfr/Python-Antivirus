url = input("Enter URL Address: ")
# def open_website(url):
#     scan_response = scan_url(url)
#     resource = scan_response.get('resource')
#     if resource:
#         scan_result = scan_results(resource)
#         positives = scan_result.get('positives')
#         if positives > 0:
#             print(f'{positives} out of {scan_result.get("total")} scanners found this URL to be malicious.')
#         else:
#             print('This URL is not malicious.')
#             webbrowser.open(url)
#     else:
#         print(scan_response)