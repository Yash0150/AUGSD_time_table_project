import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import Divider from '@material-ui/core/Divider';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';


const useStyles = makeStyles(theme =>({
    root: {
        textAlign: 'center',
        width: '100%',
        ...theme.typography.button,
        backgroundColor: theme.palette.background.paper,
        padding: theme.spacing(1),
    },
    title: {
      fontSize: 18,
      fontWeight: '500',
      textTransform: 'capitalize',
      textAlign: 'center'
    },
    pos: {
      marginBottom: 12,
    },
    courseButton: {
        display: 'flex',
        margin: 'auto',
        width: '100%'
    },
    heading: {
        marginBottom: 22,
    }
  }));

const CourseList = () => {

    const courses = ['cdc1','cdc2','cdc3','cdc1','cdc2','cdc3','cdc1','cdc2','cdc3','cdc1','cdc2','cdc3','cdc1','cdc2','cdc3','cdc1','cdc2','cdc3',]
    const classes = useStyles();
    return (
        <Card className={classes.root}>
        <CardContent>
            <Typography variant="h5" className={classes.heading} >
                Available Courses
            </Typography>
            {courses.map(course =>{
                return (
                    <Button className={classes.courseButton} >
                        <Typography className={classes.title} color="textSecondary" gutterBottom>
                            {course}
                        </Typography>
                    </Button>
                );
            })}
        </CardContent>
        </Card>
    );
}

export default CourseList;
