#include <iostream>
#include <curl/curl.h>

int main(int argc, char *argv[])
{
  curl_global_init(CURL_GLOBAL_DEFAULT);
  curl_global_cleanup();

  return EXIT_SUCCESS;
}