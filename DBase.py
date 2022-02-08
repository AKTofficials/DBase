"""
DBase 1.0.0
For making De-centralised DB.
Author : Merwin
"""

import socket
import spv
import DB_utils

class DB:
    def __init__(self,port=2323):
        pass
    #Sub_server related
    """
    For becoming a DBase sub-server. 
    The password is only needed if the server wants.
    """
    def join_server(self,server_name,server_password=None):
        pass
    """
    For stopping the activity as a sub-server.
    """
    def stop_sub_server(self):
        pass
    #De-DB related
    """
    Create a new De-DB.
    sub_server_pass is False , it is used to set 
    if the server want a sub_server with auth.
    """
    def set_up(self,server_name,server_password,sub_server_pass=False):
        pass
    """
    Start.
    """
    def start(self):
        pass
    """
    A collection is like a folder 
    for saving files.
    """
    def make_collection(self,ID):
        pass
    """
    To save a file to De-DB.
    filename it is the name of the file.
    fileid it is is the name of the file
    at server.
    collection is a group/folder in which
    the file is put into, by default
    'SAVED_FILES'.
    """
    def save_file(self,filename,fileid,collection="SAVED_FILES"):
        pass
    """
    Create class (a folder for saving info)
    """
    def make_class(self,ID):
        pass
    """
    Create Column.
    class_ is the id of class u want to
    add the column to.
    """
    def create_column(self,ID,class_):
        pass
    """
    Create a new row. 
    """
    def create_row(self,data,column,class_):
        pass
    """
    Get all columns in a class.
    """
    def get_all_columns(self,class_):
        pass
    """
    Get all rows in a column.
    """
    def get_all_rows(self,column):
        pass
    """
    Get all files in a collection.
    """
    def get_all_files(self,collection):
        pass
    """
    Get all collections.
    """
    def get_all_collections(self):
        pass
    """
    Get all classes.
    """
    def get_all_class(self):
        pass
    #server utils

    """
    Ban sub-server.
    """
    def ban_sub_server(self,ip):
        pass
    """
    List of sub-servers and their info.
    """
    def sub_server_list(self):
        pass
    #PassBin
    """
    Pass Bin is a feature to save 
    passwords in a decentralised
    way.
    """
    """
    Create a passbin.
    ID the name of the passbin.
    """
    def Create_pass_bin(self,ID):
        pass
    """
    Save to a passbin.
    """
    def PASS_BIN_ADD(self,ID_PASS_BIN,ID,password):
        pass
    """
    Varify password.
    """
    def PASS_BIN_CHECK(self,ID_PASS_BIN,ID,password):
        pass
