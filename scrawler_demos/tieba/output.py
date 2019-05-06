# -*- coding=utf-8 -*-


class Output(object):

    def save_to_db(self, document):
        '''

        :param document:
        :return:
        '''
        pass

    def save_to_html(self, file_name, data):

        if data is None or len(data) == 0:
            return 
        print "start to save data to " + file_name
        fout = open(file_name, 'w')
        fout.write("<html>")
        fout.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
        fout.write("<body>")
        fout.write("<table>")

        fout.write("<tr>")
        fout.write("<td>%s</td>" % 'number')
        fout.write('<td>%s</td>' % 'title')
        fout.write('<td>%s</td>' % 'url')
        fout.write("</tr>")

        for item in data:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % item.number)
            fout.write('<td>%s</td>' % item.title)
            fout.write('<td><a href=\'%s\'>地址</a></td>' % item.url)
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()
        print "complete to save"

    def save_to_text(self, file_name, data):

        '''
        save data to file
        :param file_name:
        :param data: PostStatisticInfo []
        :return:
        '''

        print "saving data to " + file_name

        valid_data = ''
        for item in data:
            valid_data = valid_data + item.get_data().encode('utf-8')+'\n'

        file_save = open(file_name, 'w')
        file_save.write(valid_data)
        file_save.close()
        print "complete to save"
