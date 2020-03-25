import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActions';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';

function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <Typography
      component="div"
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && <Box p={3}>{children}</Box>}
    </Typography>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired,
};

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper,
  },
  button: {
      width: '100%',
      margin: 'auto'
  }
}));

export default function SimpleTabs(props) {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  const CDC = props.state.department_cdc_list;
  const Electives = props.state.department_elective_list;

  const sortFunction = (a, b) => {
    return a.name.localeCompare(b.name);
  }

  Electives.sort(sortFunction);
  CDC.sort(sortFunction);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  const handleClick = (course) =>{
      props.setSelectedCourse(course.name);
      let course_type;
      if(value == 0)
      course_type = 'C';
      else
      course_type = 'E'
      props.setCourseInfo({...props.courseInfo,course_type,course_code:course.code});
  }

  const getCourseList = (courses) => {
      const coursesCardItems = courses.map(course => {
          return (<CardActions key={course.code}>
                    <Button className={classes.button} value={course} onClick={(event) => handleClick(course) }  >
                      {course.name} {`(${course.code})`}
                    </Button>
                </CardActions>);
      })

      return (
        <Card>
            {coursesCardItems}
        </Card>
      );
  }
  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Tabs value={value} onChange={handleChange} aria-label="simple tabs example">
          <Tab label="CDC" {...a11yProps(0)} />
          <Tab label="Electives" {...a11yProps(1)} />
        </Tabs>
      </AppBar>
      <TabPanel value={value} index={0}>
        {getCourseList(CDC)}
      </TabPanel>
      <TabPanel value={value} index={1}>
      {getCourseList(Electives)}
      </TabPanel>
    </div>
  );
}