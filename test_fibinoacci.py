from FibinoacciSeries import FibinoacciSeries
import logging




def test_to_print_fseries():
    fobject = FibinoacciSeries(3)
    output_list = fobject.to_print_fseries()
    assert output_list == [0,1,1]
    logging.info("Actual result is equal to Expected result")