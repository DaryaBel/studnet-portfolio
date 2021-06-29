import gql from "graphql-tag";

// Все университеты
export const UNIVERSITIES = gql`
  {
    allUniversities {
      id
      fullname
      shortname
      location
      description
    }
  }
`;

// Все университеты (кратко)
export const SHORTUNIVERSITIES = gql`
  {
    allUniversities {
      id
      fullname
    }
  }
`;

// Все факультеты
export const FACULTIES = gql`
  {
    allFaculties {
      id
      name
      university {
        id
        fullname
      }
      description
    }
  }
`;

// Все факультеты (кратко)
export const SHORTFACULTIES = gql`
  {
    allFaculties {
      id
      name
    }
  }
`;

// Все специальности
export const SPECIALIZATIONS = gql`
  {
    allSpecializations {
      id
      name
      codeName
      faculty {
        id
        name
      }
    }
  }
`;

// Все специальности (кратко)
export const SHORTSPECIALIZATIONS = gql`
  {
    allSpecializations {
      id
      name
    }
  }
`;

// Все группы
export const GROUPS = gql`
  {
    allGroups {
      id
      course
      formEducation
      codeName
      studyDegree
      specialization {
        id
        name
      }
    }
  }
`;

// Все группы (кратко)
export const SHORTGROUPS = gql`
  {
    allGroups {
      id
      codeName
    }
  }
`;

// Все студенты (кратко)
export const SHORTSTUDENTS = gql`
  {
    allStudents {
      id
      fullname
    }
  }
`;

// Все мероприятия
export const EVENTS = gql`
  {
    allEvents {
      id
      name
      location
      description
      date
    }
  }
`;

// Все мероприятия (кратко)
export const SHORTEVENTS = gql`
  {
    allEvents {
      id
      name
    }
  }
`;

// Все проекты
export const PROJECTS = gql`
  {
    allProjects {
      id
      name
      description
      dateStart
      dateEnd
      links
    }
  }
`;

// Все проекты (кратко)
export const SHORTPROJECTS = gql`
  {
    allProjects {
      id
      name
    }
  }
`;

// Все команды
export const TEAMS = gql`
  {
    allTeams {
      id
      name
      project {
        id
        name
      }
      participants {
        id
        fullname
      }
    }
  }
`;

// Все команды (кратко)
export const SHORTTEAMS = gql`
  {
    allTeams {
      id
      name
      participants {
        id
      }
      project {
        id
      }
    }
  }
`;

// Все студенты в мероприятиях
export const STUDENTSINEVENTS = gql`
  {
    allStudentsInEvents {
      id
      role
      event {
        id
        name
      }
      student {
        id
        fullname
      }
    }
  }
`;

// Все факультеты выбранного университета
export const FACULTIESOFUNIVERSITY = gql`
  query ($universityId: ID!) {
    university(universityId: $universityId) {
      id
      facultiesOfUniversity {
        id
        name
        description
      }
    }
  }
`;

// Все специальности выбранного факультеты
export const SPECIALIZATIONSOFFACULTY = gql`
  query ($facultyId: ID!) {
    faculty(facultyId: $facultyId) {
      id
      specializationsOfFaculty {
        id
        codeName
        name
      }
    }
  }
`;

// Все группы выбранной специальности
export const GROUPOFSPECIALIZATION = gql`
  query ($specializationId: ID!) {
    specialization(specializationId: $specializationId) {
      id
      groupsOfSpecialization {
        id
        codeName
        course
        formEducation
        studyDegree
      }
    }
  }
`;

// Все студенты выбранной группы
export const STUDENTSOFGROUP = gql`
  query ($groupId: ID!) {
    group(groupId: $groupId) {
      id
      studentsOfGroup {
        id
        fullname
        birthdate
        email
        budgetary
      }
    }
  }
`;

// Студент и его портфолио
export const PORTFOLIO = gql`
  query ($studentId: ID!) {
    student(studentId: $studentId) {
      id
      fullname
      birthdate
      email
      budgetary
      studentsForTeam {
        id
        name
        project {
          name
          description
          links
          dateStart
          dateEnd
        }
      }
      studentsInEvents {
        id
        role
        event {
          name
          date
        }
      }
    }
  }
`;

//**  МУТАЦИИ **//

// Добавить студента к участию в мероприятии
export const CREATESTUDENTINEVENT = gql`
  mutation ($event: ID!, $role: String!, $student: ID!) {
    createStudentInEvent(event: $event, role: $role, student: $student) {
      ok
    }
  }
`;

// Добавить проект
export const CREATEPROJECT = gql`
  mutation (
    $name: String!
    $description: String!
    $dateStart: Date!
    $dateEnd: Date!
    $links: String!
  ) {
    createProject(
      name: $name
      description: $description
      dateStart: $dateStart
      dateEnd: $dateEnd
      links: $links
    ) {
      project {
        id
      }
    }
  }
`;

// Добавить университет
export const CREATEUNIVERSITY = gql`
  mutation (
    $fullname: String!
    $description: String!
    $shortname: String!
    $location: String!
  ) {
    createUniversity(
      fullname: $fullname
      description: $description
      shortname: $shortname
      location: $location
    ) {
      ok
    }
  }
`;

// Добавить факультет
export const CREATEFACULTY = gql`
  mutation ($name: String!, $description: String!, $university: ID!) {
    createFaculty(
      name: $name
      description: $description
      university: $university
    ) {
      ok
    }
  }
`;

// Добавить специальность
export const CREATESPECIALIZATION = gql`
  mutation ($name: String!, $codeName: String!, $faculty: ID!) {
    createSpecialization(name: $name, codeName: $codeName, faculty: $faculty) {
      ok
    }
  }
`;

// Добавить группу
export const CREATEGROUP = gql`
  mutation (
    $codeName: String!
    $course: Int!
    $formEducation: String!
    $studyDegree: String!
    $specialization: ID!
  ) {
    createGroup(
      course: $course
      codeName: $codeName
      specialization: $specialization
      formEducation: $formEducation
      studyDegree: $studyDegree
    ) {
      ok
    }
  }
`;

// Добавить мероприятие
export const CREATEEVENT = gql`
  mutation (
    $name: String!
    $description: String!
    $date: Date!
    $location: String!
  ) {
    createEvent(
      name: $name
      description: $description
      date: $date
      location: $location
    ) {
      ok
    }
  }
`;

// Добавить команду
export const CREATETEAM = gql`
  mutation ($name: String!, $project: ID!) {
    createTeam(name: $name, project: $project) {
      ok
    }
  }
`;

// Добавить команду с участником
export const CREATETEAMWITHPERSONS = gql`
  mutation ($name: String!, $project: ID!, $participants: [ID]) {
    createTeamWithPersons(
      name: $name
      project: $project
      participants: $participants
    ) {
      ok
    }
  }
`;

// Добавить студента в команду
export const ADDTOTEAM = gql`
  mutation ($participants: [ID], $teamId: ID!) {
    addToTeam(participants: $participants, teamId: $teamId) {
      ok
    }
  }
`;

// Удалить университет
export const DELETEUNIVERSITY = gql`
  mutation ($universityId: ID!) {
    deleteUniversity(universityId: $universityId) {
      ok
    }
  }
`;

// Удалить факультет
export const DELETEFACULTY = gql`
  mutation ($facultyId: ID!) {
    deleteFaculty(facultyId: $facultyId) {
      ok
    }
  }
`;

// Удалить специальность
export const DELETESPECIALIZATION = gql`
  mutation ($specializationId: ID!) {
    deleteSpecialization(specializationId: $specializationId) {
      ok
    }
  }
`;

// Удалить группу
export const DELETEGROUP = gql`
  mutation ($groupId: ID!) {
    deleteGroup(groupId: $groupId) {
      ok
    }
  }
`;

// Удалить мероприятие
export const DELETEEVENT = gql`
  mutation ($eventId: ID!) {
    deleteEvent(eventId: $eventId) {
      ok
    }
  }
`;

// Удалить участие студента в мероприятии
export const DELETESTUDENTINEVENT = gql`
  mutation ($studentInEventId: ID!) {
    deleteStudentInEvent(studentInEventId: $studentInEventId) {
      ok
    }
  }
`;

// Удалить команду
export const DELETETEAM = gql`
  mutation ($teamId: ID!) {
    deleteTeam(teamId: $teamId) {
      ok
    }
  }
`;

// Удалить проект
export const DELETEPROJECT = gql`
  mutation ($projectId: ID!) {
    deleteProject(projectId: $projectId) {
      ok
    }
  }
`;

// Обновить мероприятие
export const UPDATEEVENT = gql`
  mutation (
    $eventId: ID!
    $name: String!
    $description: String!
    $date: Date!
    $location: String!
  ) {
    updateEvent(
      eventId: $eventId
      name: $name
      description: $description
      date: $date
      location: $location
    ) {
      ok
    }
  }
`;

// Обновить участие студента в мероприятии
export const UPDATESTUDENTINEVENT = gql`
  mutation (
    $event: ID!
    $role: String!
    $student: ID!
    $studentInEventId: ID!
  ) {
    updateStudentInEvent(
      event: $event
      role: $role
      student: $student
      studentInEventId: $studentInEventId
    ) {
      ok
    }
  }
`;

// Обновить команду
export const UPDATETEAM = gql`
  mutation ($teamId: ID!, $name: String!, $project: ID!) {
    updateTeam(teamId: $teamId, name: $name, project: $project) {
      ok
    }
  }
`;

// Обновить проект
export const UPDATEPROJECT = gql`
  mutation (
    $dateEnd: Date!
    $dateStart: Date!
    $description: String!
    $links: String!
    $name: String!
    $projectId: ID!
  ) {
    updateProject(
      dateEnd: $dateEnd
      dateStart: $dateStart
      description: $description
      links: $links
      name: $name
      projectId: $projectId
    ) {
      ok
    }
  }
`;

// Обновить университет
export const UPDATEUNIVERSITY = gql`
  mutation (
    $description: String!
    $fullname: String!
    $location: String!
    $universityId: ID!
  ) {
    updateUniversity(
      description: $description
      fullname: $fullname
      location: $location
      universityId: $universityId
    ) {
      ok
    }
  }
`;

// Обновить факультет
export const UPDATEFACULTY = gql`
  mutation (
    $description: String!
    $name: String!
    $facultyId: ID!
    $university: ID!
  ) {
    updateFaculty(
      description: $description
      name: $name
      university: $university
      facultyId: $facultyId
    ) {
      ok
    }
  }
`;

// Обновить специальность
export const UPDATESPECIALIZATION = gql`
  mutation (
    $codeName: String!
    $name: String!
    $faculty: ID!
    $specializationId: ID!
  ) {
    updateSpecialization(
      codeName: $codeName
      name: $name
      faculty: $faculty
      specializationId: $specializationId
    ) {
      ok
    }
  }
`;

// Обновить группу
export const UPDATEGROUP = gql`
  mutation (
    $codeName: String!
    $course: Int!
    $formEducation: String!
    $groupId: ID!
    $specialization: ID!
    $studyDegree: String!
  ) {
    updateGroup(
      codeName: $codeName
      course: $course
      formEducation: $formEducation
      groupId: $groupId
      specialization: $specialization
      studyDegree: $studyDegree
    ) {
      ok
    }
  }
`;
