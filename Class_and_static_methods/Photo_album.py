class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(self.pages)]
        self.page_index = 0
        print(self.photos)

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = photos_count // 4
        return cls(pages)

    def open_spot(self):    # return True/False for open spot for picture
        return self.page_index < self.pages and len(self.photos[self.page_index]) < 4

    def add_photo(self, label: str):
        if not self.open_spot():
            self.page_index += 1
        if self.page_index == self.pages and len(self.photos) == self.pages:
            return "No more free slots"
        self.photos[self.page_index].append(label)
        # print(self.photos)
        return f"{label} photo added successfully on page {self.page_index+1} slot {len(self.photos[self.page_index])}"

    def display(self):
        string = ''
        dash = "-----------\n"
        nl = "\n"
        picture = "[] "
        for _ in self.photos:
            string += dash + ''.join(picture for p in range(len(_))).strip() + nl
        string += dash

        return string


album = PhotoAlbum(4)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

# import unittest
#
#
# class TestsPhotoAlbum(unittest.TestCase):
#     def test_init_creates_all_attributes(self):
#         album = PhotoAlbum(2)
#         self.assertEqual(album.pages, 2)
#         self.assertEqual(album.photos, [[], []])
#
#     def test_from_photos_should_create_instace(self):
#         album = PhotoAlbum.from_photos_count(12)
#         self.assertEqual(album.pages, 3)
#         self.assertEqual(album.photos, [[], [], []])
#
#     def test_add_photo_with_no_free_spots(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         result = album.add_photo("prom")
#         self.assertEqual(result, "No more free slots")
#
#     def test_add_photo_with_free_spots(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])
#
#     def test_display_with_one_page(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         result = album.display().strip()
#         self.assertEqual(result, "-----------\n[] [] [] []\n-----------")
#
#     def test_display_with_three_pages(self):
#         album = PhotoAlbum(3)
#         for _ in range(8):
#             album.add_photo("asdf")
#         result = album.display().strip()
#         self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")
#
#
# if __name__ == "__main__":
#     unittest.main()
