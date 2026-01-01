import sys
import unittest
from logmaster import read_txt, write_txt, scan_log, show_stats, clean_log, monitor_log

sys.stdout = open('/dev/null', 'w')

class TestLogMaster(unittest.TestCase):

    # read and write
    def test_read_txt(self):
        data = read_txt("test/test_logs/test_log.log")
        self.assertTrue(len(data) > 0)

    def test_write_txt(self):
        write_txt("test/test_logs/w.txt", "hello")
        self.assertEqual(read_txt("test/test_logs/w.txt")[0], "hello")
    
    def test_read_txt_missing_file(self):
        self.assertEqual(read_txt("no/such/file.log"), None)

    # scan
    def test_scan_ip(self):
        scan_log("test/test_logs/test_log.log", "ip")
        self.assertTrue(len(read_txt("test/test_logs/test_log.log")) > 0)

    def test_scan_url(self):
        scan_log("test/test_logs/test_log.log", "url")
        self.assertTrue(len(read_txt("test/test_logs/test_log.log")) > 0)

    def test_scan_errors(self):
        scan_log("test/test_logs/test_log.log", "errors")
        self.assertTrue(len(read_txt("test/test_logs/test_log.log")) > 0)

    def test_scan_count(self):
        scan_log("test/test_logs/test_log.log", "url", show_count=True)
        self.assertTrue(True)

    def test_scan_export(self):
        scan_log("test/test_logs/test_log.log", "ip", export_file="test/test_logs/out1.txt")
        self.assertTrue(len(read_txt("test/test_logs/out1.txt")) > 0)

    def test_scan_file_not_found(self):
        scan_log("no/such/file.log")
        self.assertTrue(True)

    def test_scan_invalid_mode(self):
        scan_log("test/test_logs/test_log.log", "WRONG")
        self.assertTrue(True)

    def test_scan_empty_file(self):
        write_txt("test/test_logs/empty.log", "")
        scan_log("test/test_logs/empty.log", "ip")
        self.assertTrue(True)

    # stats
    def test_stats(self):
        show_stats("test/test_logs/test_log.log")
        self.assertTrue(True)

    def test_stats_export(self):
        show_stats("test/test_logs/test_log.log", export_file="test/test_logs/out2.txt")
        self.assertTrue(len(read_txt("test/test_logs/out2.txt")) > 0)

    def test_stats_file_not_found(self):
        show_stats("no/such/file.log")
        self.assertTrue(True)

    # clean
    def test_clean_remove_ip(self):
        clean_log("test/test_logs/test_log.log", remove_ip=True, export_file="test/test_logs/c1.txt")
        text = "".join(read_txt("test/test_logs/c1.txt"))
        self.assertNotIn("192.168.1.55", text)

    def test_clean_remove_ts(self):
        clean_log("test/test_logs/test_log.log", remove_timestamps=True, export_file="test/test_logs/c2.txt")
        text = "".join(read_txt("test/test_logs/c2.txt"))
        self.assertNotIn("[12/Feb", text)

    def test_clean_mask_email(self):
        clean_log("test/test_logs/test_log.log", mask_email=True, export_file="test/test_logs/c3.txt")
        text = "".join(read_txt("test/test_logs/c3.txt"))
        self.assertIn("[REDACTED EMAIL]", text)

    def test_clean_extract_api(self):
        clean_log("test/test_logs/test_log.log", extract_api=True, export_file="test/test_logs/c4.txt")
        text = "".join(read_txt("test/test_logs/c4.txt"))
        self.assertIn("/api/", text)

    def test_clean_export(self):
        clean_log("test/test_logs/test_log.log", export_file="test/test_logs/c5.txt")
        self.assertTrue(len(read_txt("test/test_logs/c5.txt")) > 0)
    
    def test_clean_file_not_found(self):
        clean_log("no/such/file.log")
        self.assertTrue(True)

    # monitor
    def test_monitor_file_not_found(self):
        monitor_log("no/such/file.log")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()