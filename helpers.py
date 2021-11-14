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
    when t.code like '\d\d__' then 0
    else 1
  end
  ),
  (
  case
    when t.code like '__x_' then 0
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

def getOrgunitsProgram(db,pg_id):
  cur = db.cursor()
  qry = """
  select o.longname
  from   Programs p
         join Orgunits o on p.offeredby = o.id
  where  p.id = %s
  """
  cur.execute(qry,[pg_id])
  info = cur.fetchone()
  cur.close()
  if not info:
    return None
  else:
    return info

def getOrgunitsStream(db,st_id):
  cur = db.cursor()
  qry = """
  select o.longname
  from   Streams s
         join Orgunits o on s.offeredby = o.id
  where  s.id = %s
  """
  cur.execute(qry,[st_id])
  info = cur.fetchone()
  cur.close()
  if not info:
    return None
  else:
    return info

def getProgramDetails(db,pg_id):
  cur = db.cursor()
  qry = """
  select aog.name, aog.definition, r.name, r.min_req
  from programs p
          join program_rules pr on p.id = pr.program
          join rules r on pr.rule = r.id
          join academic_object_groups aog on aog.id = r.ao_group
  where p.id = %s
  """
  cur.execute(qry,[pg_id])
  info = cur.fetchall()

  cur.close()
  if not info:
    return None
  else:
    return info

def getStreamDetails(db,st_id):
  cur = db.cursor()
  qry = """
  select aog.name, aog.definition, r.name, r.min_req, r.max_req
  from streams s
          join stream_rules sr on s.id = sr.stream
          join rules r on sr.rule = r.id
          join academic_object_groups aog on aog.id = r.ao_group
  where s.id = %s
  """
  cur.execute(qry,[st_id])
  info = cur.fetchall()

  cur.close()
  if not info:
    return None
  else:
    return info

def getDegreeName(db, stream_code):
  cur = db.cursor()
  qry = """
  select s.name
  from streams s
  where s.code = %s
  """
  cur.execute(qry,[stream_code])
  info = cur.fetchone()

  cur.close()
  if not info:
    return None
  else:
    return info

def getCourseName(db, course_code):
  cur = db.cursor()
  qry = """
  select s.name
  from subjects s
  where s.code = %s
  """
  cur.execute(qry,[course_code])
  info = cur.fetchone()

  cur.close()
  if not info:
    return None
  else:
    return info

def getType(db, pg_id):
  cur = db.cursor()
  qry = """
  select aog.type
  from programs p
          join program_rules pr on p.id = pr.program
          join rules r on pr.rule = r.id
          join academic_object_groups aog on aog.id = r.ao_group
  where p.id = %s
  """
  cur.execute(qry,[pg_id])
  info = cur.fetchone()

  cur.close()
  if not info:
    return None
  else:
    return info

def getStreamType(db, st_id):
  cur = db.cursor()
  qry = """
  select s.stype
  from streams s
  where s.name = %s
  """
  cur.execute(qry,[st_id])
  info = cur.fetchone()

  cur.close()
  if not info:
    return None
  else:
    return info

def getStreamRulesType(db, st_id):
  cur = db.cursor()
  qry = """
  select r.type
  from streams s
          join stream_rules sr on sr.stream = s.id
          join rules r on r.id = sr.rule
  where s.id = %s
  """
  cur.execute(qry,[st_id])
  info = cur.fetchone()

  cur.close()
  if not info:
    return None
  else:
    return info

def getProgramRulesType(db, pg_id):
  cur = db.cursor()
  qry = """
  select r.type
  from programs p
          join program_rules pr on pr.program = p.id
          join rules r on r.id = pr.rule
  where p.id = %s
  """
  cur.execute(qry,[pg_id])
  info = cur.fetchone()

  cur.close()
  if not info:
    return None
  else:
    return info

def getRulesType(db, name):
  cur = db.cursor()
  qry = """
  select r.type
  from rules r
  where r.name = %s
  """
  cur.execute(qry,[name])
  info = cur.fetchone()

  cur.close()
  if not info:
    return None
  else:
    return info

def getAogDefby(db, name):
  cur = db.cursor()
  qry = """
  select a.defby
  from academic_object_groups a
  where a.name = %s
  """
  cur.execute(qry,[name])
  info = cur.fetchone()

  cur.close()
  if not info:
    return None
  else:
    return info

def minOrMax(min, max, course):
    # min and max are null ... nothing to be displayed
    if not min and not max:
      pass
    # min is not null, max is null ... "at least min"
    elif min and not max:
      print(f"at least {min} UOC courses from {course}")
    # min is null, max is not null ... "up to max"
    elif not min and max:
      print(f"up to {max} UOC courses from {course}")
    # both are not null and min < max ... "between min and max"
    elif min and max and min < max:
      print(f"between {min} and {max} UOC courses from {course}")
    # both are not null and min = max ... "min"
    elif min and max and min == max:
      print(f"{min} UOC courses from {course}")

def minOrMaxFree(min, max, course):
    # min and max are null ... nothing to be displayed
    if not min and not max:
      pass
    # min is not null, max is null ... "at least min"
    elif min and not max:
      print(f"at least {min} UOC of {course}")
    # min is null, max is not null ... "up to max"
    elif not min and max:
      print(f"up to {max} UOC of {course}")
    # both are not null and min < max ... "between min and max"
    elif min and max and min < max:
      print(f"between {min} and {max} UOC of {course}")
    # both are not null and min = max ... "min"
    elif min and max and min == max:
      print(f"{min} UOC of {course}")