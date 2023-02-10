import json
import os
import sys

try:
    REF = sys.argv[1]
    BRANCH = REF.split("/")[2]
except:
    BRANCH = 'main'

class UpdateReadmeFile:
    DIFICULTIES = {
        '1': 'Easy',
        '2': 'Medium',
        '3': 'Hard'
    }
    GITHUB_BASE_URL = 'https://github.com/caramelthunder/leetcodeBlind75/tree/{}/src/'.format(BRANCH)
    GITHUB_QUICKLINKS = 'https://github.com/caramelthunder/leetcodeBlind75/tree/{}#'.format(BRANCH)
    ROW_TEMPLATES = {
        1 : '|{}|[{}]({})|**{}**|[Solution]({}{}/solutions/{})|[Test]({}{}/unittest/{})|\n',
        2 : '|{}|[{}]({})|**{}**|[Sol 1]({}{}/solutions/{}), [Sol 2]({}{}/solutions/{})|[Test]({}{}/unittest/{})|\n',
        3 : '|{}|[{}]({})|**{}**|[Sol 1]({}{}/solutions/{}), [Sol 2]({}{}/solutions/{}), [Sol 3]({}{}/solutions/{})|[Test]({}{}/unittest/{})|\n'
    }

    def __init__(self, filename):
        # print('----The current branch is'.format(BRANCH))
        # print('----The current working Dir is'.format(os.getcwd()))
        self.filename = filename
        self.index = {}
        self.scan_folders()
    
    def extract_numbers(self, s):
        return int(s.split("_")[1])

    def get_folder_names(self, dir= os.getcwd() + '/src', prefix= 'leetcode_'):
        folders = []
        for folder in os.listdir(dir):
            print(folder)
            if folder.startswith(prefix):
                folders.append(folder)
        return folders

    def get_metadada(self, folder, dir= os.getcwd()) -> dict:
        # print('---Getting ' + dir + '/src/' + folder + '/.metadata.json')
        # print(os.listdir(dir + '/src/' + folder))
        metadata = {}
        try:
            with open(dir + '/src/' + folder + '/.metadata.json', 'r') as f:
                data = json.load(f)
                metadata['id'] = self.extract_numbers(folder)
                metadata['folder'] = folder
                metadata['name'] = data.get('name', '')
                metadata['leetcode_url'] = data.get('leetcode_url', '')
                metadata['level'] = data.get('level', '')
                metadata['topics'] = data.get('topics', [])

                solutions_path = '{}/src/{}/solutions'.format(dir, folder)
                for file in self.get_folder_names(solutions_path):
                    if file.endswith('.py') and not file.startswith('__init__'):
                        metadata['solutions'] = metadata.get('solutions', [])
                        metadata['solutions'].append(file)

                unittest_path = '{}/src/{}/unittest'.format(dir, folder)
                for file in self.get_folder_names(unittest_path):
                    if file.endswith('.py'):
                        metadata['unittest'] = file

        except FileNotFoundError:
            print(dir + '/src/' + folder + '/.metadata.json')
            print('".metadata.json" does not exist in {}/'.format(folder))

        return metadata

    def scan_folders(self, dir= os.getcwd()):
        self.index = {'all': [], 'topics': {}, 'levels': {'Easy': [], 'Medium': [], 'Hard': []}}

        folders = self.get_folder_names(prefix= 'leetcode_')
        for folder in folders:
            #dir = '/'.join(dir.split("/")[:-1])
            metadata = self.get_metadada(folder, dir)
            if metadata:
                id = metadata.get('id', float('inf'))
                level = self.DIFICULTIES[metadata.get('level', "1")]
                topics = metadata.get('topics', [])

                self.index['all'].append((id, metadata))

                self.index['levels'][level] = self.index['levels'].get(level, [])
                self.index['levels'][level].append((id, metadata))

                for topic in topics:
                    self.index['topics'][topic] = self.index['topics'].get(topic, [])
                    self.index['topics'][topic].append((metadata.get('level', "1"), id, metadata))

    def create_header(self):
        with open(self.filename, 'w') as readme:
            header =  '<div align="center">\n'
            header += '<h2>LeetCode Blind 75 Questions and More</h2>\n'
            header += '<h5>By Thinh Nguyen test _1</h5>\n'
            header += '</div>\n'
            header += '\n'
            readme.write(header)
            
    def create_quick_links(self):

        def text_process(s: str):
            s = s.lower().replace('(', '').replace(')', '').replace(' ', '-')
            return s

        with open(self.filename, 'a') as readme:
            quicklinks = '***\n'
            for key in self.index:
                if key == 'topics':
                    for topic in self.index['topics']:
                        quicklinks += '[{}]({}{})  |  '.format(topic, self.GITHUB_QUICKLINKS, text_process(topic))
                    
                elif key == 'levels':
                    for level in self.index['levels']:
                        quicklinks += '[{}]({}{})  |  '.format(level, self.GITHUB_QUICKLINKS, text_process(level))
            
            quicklinks += '\n'      
            quicklinks += '***\n'
            readme.write(quicklinks)

    def create_table_row(self, metadata, row_template= 1):
        def template_1():
            row = self.ROW_TEMPLATES[row_template]
            row = row.format(
                metadata.get('id', ''),
                metadata.get('name', ''),
                metadata.get('leetcode_url', ''),
                self.DIFICULTIES[metadata.get('level', '')],
                self.GITHUB_BASE_URL,
                metadata.get('folder', ''),
                metadata['solutions'][0],
                self.GITHUB_BASE_URL,
                metadata.get('folder', ''),
                metadata.get('unittest', '')
            )
            return row

        def template_2():
            row = self.ROW_TEMPLATES[row_template]
            row = row.format(
                metadata.get('id', ''),
                metadata.get('name', ''),
                metadata.get('leetcode_url', ''),
                self.DIFICULTIES[metadata.get('level', '')],
                self.GITHUB_BASE_URL,
                metadata.get('folder', ''),
                metadata['solutions'][0],
                self.GITHUB_BASE_URL,
                metadata.get('folder', ''),
                metadata['solutions'][1],
                self.GITHUB_BASE_URL,
                metadata.get('folder', ''),
                metadata.get('unittest', '')
            )
            return row

        def template_3():
            row = self.ROW_TEMPLATES[row_template]
            row = row.format(
                metadata.get('id', ''),
                metadata.get('name', ''),
                metadata.get('leetcode_url', ''),
                self.DIFICULTIES[metadata.get('level', '')],
                self.GITHUB_BASE_URL,
                metadata.get('folder', ''),
                metadata['solutions'][0],
                self.GITHUB_BASE_URL,
                metadata.get('folder', ''),
                metadata['solutions'][1],
                self.GITHUB_BASE_URL,
                metadata.get('folder', ''),
                metadata['solutions'][2],
                self.GITHUB_BASE_URL,
                metadata.get('folder', ''),
                metadata.get('unittest', '')
            )
            return row 

        switch = {
            1: template_1,
            2: template_2,
            3: template_3
        }
        return switch.get(row_template, lambda: print('Invalid template.'))()

    def create_table(self):
        with open(self.filename, 'a') as readme:
            #################--All Table--#################
            _list =  '### {}\n'.format('Blind 75')
            _list += '|LC#|Problem|Level|Python Solution(s)|Unittest|\n'
            _list += '|---|-------|-----|------------------|--------|\n'

            problems = self.index['all']
            problems.sort(key= lambda item:item[0])
            for problem in problems:
                id, metadata = problem
                num_of_solution = len(metadata.get('solutions', 0))
                row = self.create_table_row(metadata, num_of_solution)
                _list += row
            readme.write(_list)

            ###############--Levels Table--################
            levels = self.index['levels']
            for level in levels:
                _list =  '### {}\n'.format(level)
                _list += '|LC#|Problem|Level|Python Solution(s)|Unittest|\n'
                _list += '|---|-------|-----|------------------|--------|\n'

                problems = levels.get(level, [])
                problems.sort(key= lambda item:item[0])
                for problem in problems:
                    id, metadata = problem
                    num_of_solution = len(metadata.get('solutions', 0))
                    row = self.create_table_row(metadata, num_of_solution)
                    _list += row
                readme.write(_list)

            ###############--Topics Table--################
            topics = self.index['topics']
            for topic in topics:
                _list =  '### {}\n'.format(topic)
                _list += '|LC#|Problem|Level|Python Solution(s)|Unittest|\n'
                _list += '|---|-------|-----|------------------|--------|\n'

                problems = topics.get(topic, [])
                problems.sort(key= lambda item:(item[0], item[1]))
                for problem in problems:
                    level, id, metadata = problem
                    num_of_solution = len(metadata.get('solutions', 0))
                    row = self.create_table_row(metadata, num_of_solution)
                    _list += row
                readme.write(_list)

    def create_footer(self):
        with open(self.filename, 'a') as readme:
            
            footer = '## How to run `_unittest.py`\n'
            footer += 'Each solved problem have a `unittest/` folder.\n'
            footer += '\n'
            footer += 'To locate the Python test script, click on the `test` link of the problem.\n'
            footer += '\n'
            footer += 'To run the test script, add the below code and `Run` the `_unittest.py`:\n'
            footer += '\n'
            footer += '''
            if __name__ == '__main__':
                unittest.main()
            \n'''
            footer += 'You can also add more test cases by appending to the `class Test(unittest.TestCase):`\n'
            footer += '\n'
            footer += 'For example:\n'
            footer += '''
            def test_your_test_case(self):
                input_nums = [3,3]
                target = 6
                expected_output = {0,1}

                output = set(self.s.twoSum(input_nums, target))
                self.assertEqual(output, expected_output)
            \n'''
            footer += '#### Note:\n'
            footer += 'Each problem is already equipped with `helpers functions` to execute the test cases without additional dependencies.\n'
            footer += 'Please follow the format of the existing test cases when creating your own.\n'
            footer += '\n'
            footer += 'Happy coding :)\n'

            readme.write(footer)


    def update_readme(self): 
        self.create_header()
        self.create_quick_links()
        self.create_table()
        self.create_footer()


############################
if __name__ == '__main__':
    filename = 'README.md'
    r = UpdateReadmeFile(filename)
    r.update_readme()
    
    with open(filename, 'r') as readme:
        for line in readme:
            print(line)

