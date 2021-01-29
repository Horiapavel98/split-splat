from argparse import ArgumentParser

class Splitter():
    """
    Split contents of a file with up to a number of specified characters on each line.

    See argument parser for details.
    """
    @staticmethod
    def split_splat():
        parser = ArgumentParser(description="""\
        Split contents of a file with up to a number of specified characters on
        a line.
        """)

        parser.add_argument('filename', 
                            help="""Name of the file that you want to process.
                            The file can be renamed or it will be recreated""")
        parser.add_argument('-c', '--characters',
                            help="""Number of max characters that you want on each
                            line. Default is 100.""")
        parser.add_argument('-r', '--rename',
                            help="""If you want to rename the file just put the argument
                            here.""")

        args = parser.parse_args()

        filename = args.filename
        char_max = args.characters
        new_name = args.rename

        if char_max == None:
            char_max = 100
        else:
            char_max = int(char_max)
            if char_max <= 0:
                raise TypeError("Invalid argument for -c [--characters]: needs to be > 1")
        
        if not new_name:
            new_name = "output.txt"

        
        with open(filename, 'r') as f, open(new_name, 'w+') as o:
            lines = []
            for line in f:
                lines.append(line)
            
            words = []
            for line in lines:
                if line != '\n':
                    if len(line) < char_max:
                        words.append(line)    
                    else:
                        words.extend(line.split())
                else:
                    words.append(line)

            linefeed = ''
            for word in words:
                if len(linefeed) < char_max:
                    linefeed += word
                    if word == '\n':
                        o.write('\n')
                        linefeed = ''
                    elif '\n' in word:
                        # linefeed += '\n'
                        o.write(linefeed)
                        linefeed = ''
                    else:
                        linefeed += ' '
                else:
                    linefeed += '\n'
                    o.write(linefeed)
                    linefeed = ''

            if linefeed != '':
                o.write('\n')
                o.write(linefeed)
                linefeed = ''
                
        f.close()
        o.close()



if __name__ == "__main__":
    Splitter().split_splat()