/*
 * @Author: hibana2077 hibana2077@gmail.com
 * @Date: 2023-12-14 17:37:19
 * @LastEditors: hibana2077 hibana2077@gmail.com
 * @LastEditTime: 2023-12-14 17:49:03
 * @FilePath: \plant_image_collator\collator\esp32\xiao\page_control.cpp
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
#include <fstream>
#include <iostream>
#include <map>
#include <string>

// -- namespace --
using std::copy;
using std::map;
using std::string;

string get_html_context(string file_name) {
    string path = file_name + ".html";
    std::ifstream file(path);
    string context((std::istreambuf_iterator<char>(file)),
                    std::istreambuf_iterator<char>());
    return context;
}