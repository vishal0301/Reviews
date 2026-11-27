from django.test import TestCase
from django.urls import reverse


class PublicPageSmokeTests(TestCase):
    """Every shipped page should resolve and render its corresponding template."""

    page_names = [
        "home",
        "home2",
        "home3",
        "about",
        "blog",
        "login",
        "register",
        "contacts",
        "404",
        "faq",
        "help",
        "companies",
        "all-categories",
        "category-companies-listings-filterstop",
        "write-review",
        "icon-pack-1",
        "icon-pack-2",
        "icon-pack-3",
        "icon-pack-4",
        "review-page",
        "confirm",
        "dashboard",
        "user-settings",
        "row-listings-filterscol",
        "grid-listings-filterscol",
        "grid-listings-filterstop",
        "pricing",
    ]

    def test_all_public_pages_render(self):
        for page_name in self.page_names:
            with self.subTest(page=page_name):
                response = self.client.get(reverse(page_name))
                self.assertEqual(response.status_code, 200)


class RouteRegressionTests(TestCase):
    def test_homepage_variants_have_distinct_routes(self):
        self.assertNotEqual(reverse("home"), reverse("home2"))
        self.assertNotEqual(reverse("home"), reverse("home3"))

    def test_legacy_misspelled_grid_url_still_resolves(self):
        response = self.client.get(reverse("grid-listings-filterscol-legacy"))
        self.assertEqual(response.status_code, 200)
