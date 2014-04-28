import os

if __name__ == '__main__':
    posts = [post for post in os.listdir('.') if 'markdown' in post and '.swp' not in post]
    for post in posts:
        splitPost = post.split('-')
        year = splitPost[0]
        month = splitPost[1]
        day = splitPost[2]
        fileName = '-'.join(splitPost[3:])
        path = '.'
        for i in (year, month, day):
          path += '/' + i
          print i, path
          if not os.path.isdir(path):
            os.mkdir(path)

        print post, path + '/' + fileName
        os.rename(post, path + '/' + fileName)
