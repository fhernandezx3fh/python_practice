def main():
    print "First Module was run directly."
    print "First Module's Name: {}".format(__name__)

if __name__ == '__main__':
    main()

else:
    print "First Module was run from import."
    print "First Module's Name: {}".format(__name__)
