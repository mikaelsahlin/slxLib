#!/usr/bin/env python3
import xml.etree.ElementTree as et
import argparse

def make_tree(node,name):
    tree = et.TreeBuilder(element_factory=None)
    root = tree.start(name)


def node_copy(old_node):
    node = et.SubElement(old_node
    return node

def make_node(node_name,argv):
    
