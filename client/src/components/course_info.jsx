import React from 'react'
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import styled from 'styled-components';
import Autocomplete from '@material-ui/lab/Autocomplete';

const useStyles = makeStyles(theme =>({
    root: {
        textAlign: 'center',
        width: '100%',
        ...theme.typography.button,
        backgroundColor: theme.palette.background.paper,
        padding: theme.spacing(1),
        '& > *': {
            margin: theme.spacing(1),
            width: '25ch',
          },
    },
    heading: {
        marginBottom: 22,
    },
  }));

  const styles = {
    card_content: {
        margin: 'auto',
        width: '100%',
    },
    text_field: {
        margin: 'auto',
    },
    button: {
        margin: 'auto',
        marginTop: 15,
    }
  };

  const Form = styled.form`
    display: flex;
    flex-direction: column;
    margin: auto;
    width: 100%;
    justify-content: center;
  `;


export default function CourseInfo(props) {
    const classes = useStyles();
    const courseInfo = props.courseInfo;
    const setCourseInfo = props.setCourseInfo;

    const handleInfoChange = (e) => {
        console.log(courseInfo);
        const name = e.target.name;
        const value = e.target.value;
        setCourseInfo({...courseInfo,[name]: value});
    }
    const handleIcChange = (e,v) => {
        setCourseInfo({...courseInfo,ic:v.psrn_or_id});
    }
    return (
        <Card className={classes.root}>
        <CardContent style={styles.card_content}>
            <Typography variant="h5" className={classes.heading} >
                Course Info {props.selectedCourse ? `of ${props.selectedCourse}` : null}
            </Typography>
            <Form className={classes.root} noValidate>
                <TextField onChange={(event) => handleInfoChange(event)} type="Number" name="l_count" label="lectures" style={styles.text_field} />
                <TextField onChange={(event) => handleInfoChange(event)} type="Number" name="t_count" label="tutorials" style={styles.text_field}  />
                <TextField onChange={(event) => handleInfoChange(event)} type="Number" name="p_count" label="practicals" style={styles.text_field}  />
                <TextField onChange={(event) => handleInfoChange(event)} type="Number" name="student_count" label="No. of students" style={styles.text_field}  />
                <Autocomplete
                options={props.state.faculty_list}
                getOptionLabel={option => option.name}
                style={styles.text_field}
                label="IC"
                required={true}
                renderInput={params =>  <TextField style={styles.text_field} {...params} label={'IC'} />}
                onChange={(event,value) => handleIcChange(event,value)}
                />
                <TextField onChange={(event) => handleInfoChange(event)} type="Number" name="max_strength" label="Max Strength" style={styles.text_field}  />
            </Form>
        </CardContent>
        </Card>
    )
}