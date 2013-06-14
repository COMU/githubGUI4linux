import git
repo = git.Repo( '/home/mehtap/githubGUI4linux/github4linux/' )
print repo.git.status()
# checkout and track a remote branch
#print repo.git.checkout( 'origin/master', b='master' )
# add a file
#print repo.git.add('/home/mehtap/githubGUI4linux/github4linux/deneme5.py')
# commit
#print repo.git.commit( m='python kodu ile commit gonderildi5' )
# now we are one commit ahead
#print repo.git.status()
repo.git.push('https://github.com/COMU/githubGUI4linux.git','master',)
