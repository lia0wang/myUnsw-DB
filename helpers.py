# COMP3311 21T3 Ass2 ... Python helper functions
# add here any functions to share between Python scripts 
# you must submit this even if you add nothing

from re import UNICODE, subn


def getProgram(db,code):
  cur = db.cursor()
  cur.execute("select * from Programs where code = %s",[code])
  info = cur.fetchone()
  cur.close()
  if not info:
    return None
  else:
    return info

def getStream(db,code):
  cur = db.cursor()
  cur.execute("select * from Streams where code = %s",[code])
  info = cur.fetchone()
  cur.close()
  if not info:
    return None
  else:
    return info

def getStudent(db,zid):
  cur = db.cursor()
  qry = """
  select p.*, c.name
  from   People p
         join Students s on s.id = p.id
         join Countries c on p.origin = c.id
  where  p.id = %s
  """
  cur.execute(qry,[zid])
  info = cur.fetchone()
  cur.close()
  if not info:
    return None
  else:
    return info
  
def getTranscriptCourseDetail(db,zid):
  cur = db.cursor()
  qry = """
  select sub.code, t.code, sub.name, ce.mark, ce.grade, sub.uoc
  from subjects sub
          join courses c on sub.id = c.subject
          join terms t on c.term = t.id
          join course_enrolments ce on ce.course = c.id
          join students s on s.id = ce.student
  where s.id = %s
  order by 
  (
  case
    when t.code = 'x' then 0
    else 1
  end
  ), t.code
  , sub.code ASC
  """
  cur.execute(qry,[zid])
  info = cur.fetchall()

  cur.close()
  if not info:
    return None
  else:
    return info

def getUocAndWam(uoc_lst, def_uoc_lst, wam_lst):
    uoc_sum = sum(uoc_lst)

    def_uoc_sum = sum(def_uoc_lst)

    wam_sum = [a * b for a, b in zip(wam_lst, def_uoc_lst)]

    wam_average = round(sum(wam_sum) / def_uoc_sum, 1)

    return[uoc_sum, sum(wam_sum), def_uoc_sum, wam_average]

# my_seq = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'x', 's']
# def custom_key(word):
#   nums = []
#   for letter in word:
#     nums.append(my_seq.index(letter))
#   return nums
