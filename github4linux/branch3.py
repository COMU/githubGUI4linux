import git

repo = git.Repo( '/home/kancer/bohca' )
print repo.git.status()

# checkout and track a remote branch
#print repo.git.checkout( 'origin/devel', b='devel' )

print "branch: ",repo.git.branch()

# delete branch
sonuc_branch = repo.git.branch('d', 'master') # master dalini siler
print sonuc_branch

# create branch 
sonuc_create = repo.git.checkout('origin',b = 'deneme2') # deneme2 isminde bir dal olusturur ve o dala gecer. 'origin' yerine 'origin/varolan_dal_ismi' seklinde de yazilabilir.
print sonuc_create

repo.git.checkout('master') # dal degistirmek icin kullanilir. 'master' dalina gecer.

# add a file
#print repo.git.add( 'somefile' )
# commit
#print repo.git.commit( m='my commit message' )
