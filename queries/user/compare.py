from . import conn, cursor
import matplotlib.pyplot as plt

def compare_diff(u):
    
    hard = []
    medium = []
    easy = []

    solved_Hard = '''(SELECT count(problems.problem_id) FROM PROBLEMS JOIN
    (SELECT * FROM SOLVED where USER_ID = %s) result_query1
    ON PROBLEMS.PROBLEM_ID = result_query1.problem_id
    where rating_difficulty= 'Hard')'''

    solved_Medium = '''(SELECT count(problems.problem_id) FROM PROBLEMS JOIN
    (SELECT * FROM SOLVED where USER_ID = %s) result_query1
    ON PROBLEMS.PROBLEM_ID = result_query1.problem_id
    where rating_difficulty= 'Medium')'''

    solved_Easy = '''(SELECT count(problems.problem_id) FROM PROBLEMS JOIN
    (SELECT * FROM SOLVED where USER_ID = %s) result_query1
    ON PROBLEMS.PROBLEM_ID = result_query1.problem_id
    where rating_difficulty= 'Easy')'''

    for u_id in u:
        try:
            cursor.execute(solved_Hard, (u_id, ))
            hard.append(cursor.fetchall()[0][0])

            cursor.execute(solved_Medium, (u_id, ))
            medium.append(cursor.fetchall()[0][0])

            cursor.execute(solved_Easy, (u_id, ))
            easy.append(cursor.fetchall()[0][0])
        except Exception as e:
            print(e)
            continue

    width = 0.25
    fig = plt.subplots()

    br1 = [x for x in range(len(u))]
    br2 = [x + width for x in br1]
    br3 = [x + width for x in br2]

    plt.bar(br1, easy, color='r', width=width, label='Easy')
    plt.bar(br2, medium, color='g', width=width, label='Medium')
    plt.bar(br3, hard, color='b', width=width, label='Hard')

    plt.xlabel('user id')
    plt.ylabel('solves')
    plt.xticks([r + width for r in range(len(u))], u)
    plt.title('DIFFICULTY COMPARISON')

    plt.legend()
    plt.show()

def total_solves(u):
    
    solved = ''' select count(problem_ID) from solved where user_Id = %s'''
    solves = []

    for u_id in u:
        cursor.execute(solved, (u_id, ))
        solves.append(int(cursor.fetchall()[0][0]))
    
    fig = plt.figure()

    plt.bar(u, solves, width=0.4)
    plt.xlabel('user id')
    plt.ylabel('solves')
    plt.title("SOLVES COMPARISON")
    plt.show()

def tag_comparison(u):
    solved_tag = ''' select count(rq2.problem_id) from  
    (select problems_tags.problem_id,problems_tags.tag,rq1.user_id,rq1.language,rq1.date
    from problems_tags
    join
    (SELECT * FROM SOLVED where USER_ID = %s)rq1
    on rq1.problem_id=problems_tags.Problem_ID
    where problems_tags.Tag = %s)rq2'''

    tags = list(input("Enter space seperated tags for comparison: ").split())
    tags = list(set(tags))

    d = dict()
    for tag in tags:
        d[tag] = []
    
    for u_id in u:
        for tag in tags:
            try:
                cursor.execute(solved_tag, (u_id, tag))
                d[tag].append(int(cursor.fetchall()[0][0]))
            except Exception as e:
                print(e)
                continue
    
    width = 0.25
    fig = plt.subplots()

    brs = [[x for x in range(len(u))]]
    for cnt in range(len(tags) - 1):
        brs.append([x + width for x in brs[-1]])
    
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for cnt in range(len(tags)):
        plt.bar(brs[cnt], d[tags[cnt]], color=colors[cnt], width=width, label=tags[cnt])
    
    plt.xlabel('user id')
    plt.ylabel('solves')
    plt.xticks([r + width for r in range(len(u))], u)
    plt.title('TAG SOLVES COMPARISON')

    plt.legend()
    plt.show()


def compare():
    u = list(input("Enter space seperated USER-ID: ").split())

    compare_diff(u)
    total_solves(u)
    tag_comparison(u)