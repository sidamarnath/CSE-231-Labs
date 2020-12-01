import date

A = date.Date( 1, 1, 2014 )

print( A )
print( A.to_iso() )
print( A.to_mdy() )
print( A.is_valid() )
print()

B = date.Date( 12, 31, 2014 )

print( B )
print( B.to_iso() )
print( B.to_mdy() )
print( B.is_valid() )
print()

C = date.Date()

C.from_iso( "2014-07-04" )

print( C )
print( C.to_iso() )
print( C.to_mdy() )
print( C.is_valid() )
print()

D = date.Date()

D.from_mdy( "March 15, 2015" )

print( D )
print( D.to_iso() )
print( D.to_mdy() )
print( D.is_valid() )
print()

E = date.Date()

print( E )
print( E.to_iso() )
print( E.to_mdy() )
print( E.is_valid() )
print()

# testing the init function for erraneous arguments
F = date.Date(13,40,2017)
print(F)
print( F.to_iso() )
print( F.to_mdy() )
print( F.is_valid() )
print()

# testing iso function for spaces in arguments
G = date.Date()
G. from_iso("20 01 - 09 - 25")
print(G)
print( G.to_iso() )
print( G.to_mdy() )
print( G.is_valid() )
print()

# testing mdy function for spaces in argument
H = date.Date()
H. from_mdy("June         21,     2004")
print(H)
print( H.to_iso() )
print( H.to_mdy() )
print( H.is_valid() )
print()

# testing iso function for non valid arguments
I = date.Date()
I. from_iso("Garbage 66-29374")
print(I)
print( I.to_iso() )
print( I.to_mdy() )
print( I.is_valid() )
print()

# testing mdy function for non valid arguments
J = date.Date()
J. from_mdy("March ides, 2020")
print(J)
print( J.to_iso() )
print( J.to_mdy() )
print( J.is_valid() )
print()

