package life.qbic.portal.sampletracking

import com.vaadin.annotations.Theme
import com.vaadin.server.VaadinRequest
import com.vaadin.shared.ui.ContentMode
import com.vaadin.ui.Component
import com.vaadin.ui.Label
import com.vaadin.ui.Layout
import com.vaadin.ui.UI
import com.vaadin.ui.VerticalLayout
import org.apache.commons.lang3.StringUtils
import org.apache.logging.log4j.LogManager
import org.apache.logging.log4j.Logger

/**
 * This is the class from which all other QBiC portlets derive.
 */
@Theme("mytheme")
@SuppressWarnings("serial")
public abstract class QBiCPortletUI extends UI {

    /**
     * Location of the properties file where maven stores version/repository url.
     */
    public static final String PORTLET_PROPERTIES_FILE_PATH = "portlet.properties";

    /**
     * Location of the local configuration. This is useful when testing portlets loocally using {@code mvn jetty:run}.
     */
    public static final String DEVELOPER_PROPERTIES_FILE_PATH = "developer.properties";

    static final String INFO_LABEL_CLASS = "portlet-footer";
    static final String INFO_LABEL_ID = "qbic-portlet-info-label";
    static final String DEFAULT_REPO = "http://github.com/qbicsoftware";
    static final String DEFAULT_VERSION = "0.0.1-alpha";


    private static final Logger LOG = LogManager.getLogger(QBiCPortletUI.class);

    private final String portletVersion;
    private final String portletRepoURL;

    /**
     * Default constructor.
     */
    public QBiCPortletUI() {
        // load url/version from portlet.properties
        LOG.info("Initializing QBiCPortletUI");
        final Properties portletProperties = new Properties();
        try (final InputStream propertiesFileStream =
            QBiCPortletUI.class.getClassLoader().getResourceAsStream(PORTLET_PROPERTIES_FILE_PATH)) {
            portletProperties.load(propertiesFileStream);
            if (!portletProperties.containsKey("version")
                || !portletProperties.containsKey("repository.url")) {
                LOG.error("Missing version and/or repository url properties in portlet.properties file. "
                    + "The file should contain the 'version' and 'repository.url' properties. "
                    + "Using default version and/or repository url.");
            }
        } catch (final Exception e) {
            LOG.error("Error loading portlet.properties. Portlet will display bogus version/url values. "
                + "Check that portlet.properties is found under the /WEB-INF/classes folder (this file "
                + "is copied from src/main/resources/portlet.properties during the build).", e);
        }

        portletVersion =
            StringUtils.trimToEmpty(portletProperties.getProperty("version", DEFAULT_VERSION));
        portletRepoURL =
            StringUtils.trimToEmpty(portletProperties.getProperty("repository.url", DEFAULT_REPO));
    }

    @Override
    protected final void init(final VaadinRequest request) {
        LOG.info("Version " + portletVersion);
        final VerticalLayout layout = new VerticalLayout();
        layout.setMargin(false);
        // add the portlet
        layout.addComponent(getPortletContent(request));

        addPortletInfo(layout);
        setContent(layout);
    }

    @Override
    public final void setContent(final Component content) {
        super.setContent(content);
    }

    // adds version and repository information to the passed layout
    private void addPortletInfo(final Layout layout) {
        final Label portletInfoLabel = new Label("version " + portletVersion + " (<a href=\""
            + portletRepoURL + "\">" + portletRepoURL + "</a>)", ContentMode.HTML);
        portletInfoLabel.addStyleName(INFO_LABEL_CLASS);
        portletInfoLabel.setId(INFO_LABEL_ID);
        layout.addComponent(portletInfoLabel);
    }

    /**
     * Provide the content that will be displayed.
     */
    protected abstract Layout getPortletContent(final VaadinRequest request);
}
